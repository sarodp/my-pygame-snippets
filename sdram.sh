#!/bin/sh
#
echo ""
echo "\$vcgencmd measure_volts ... "
echo "-----------------------------"

for id in core sdram_c sdram_i sdram_p 
do
 echo " $id:\t$(vcgencmd measure_volts $id)"
done

echo ""
echo "\$vcgencmd measure_clock ... "
echo "-----------------------------"
for src in arm core h264 isp v3d uart pwm emmc pixel vec hdmi dpi 
do 
   echo " $src:\t$(vcgencmd measure_clock $src)" 
done


echo ""
echo "\$vcgencmd measure_temp "
echo "-----------------------------"
   echo "$(vcgencmd measure_temp)" 


echo ""
echo "\$vcgencmd get_config int "
echo "-----------------------------"
echo "$(vcgencmd get_config int)"
echo ""

echo "\$vcgencmd get_mem arm && vcgencmd get_mem gpu"
echo "-----------------------------------------------"
echo "$(vcgencmd get_mem arm && vcgencmd get_mem gpu)"
echo ""
echo ""


echo "Raspberry Pi SysInfo."
echo "---------------------"
MHZ=$(cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq)
TEMPE=$(cat /sys/class/thermal/thermal_zone0/temp)
echo Hardware:
echo CPU Speed $(($MHZ/1000)) Mhz 

TEMPS=$'\0xe2\0x84\0x83'C
echo CPU Temp $(($TEMPE/1000)) $TEMPS

