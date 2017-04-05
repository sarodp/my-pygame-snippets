#!/usr/bin/python2
#omx01.py
from omxplayer import OMXPlayer
from time import sleep

xfile1 = '/home/pi/mp4/boxes.avi'
xfile2 = '/home/pi/mp4/c.mp4'
xfile3 = '/home/pi/mp4/cat.mov'

# This will start an `omxplayer` process, this might
# fail the first time you run it, currently in the
# process of fixing this though.
#player1 = OMXPlayer(xfile1)
player2 = OMXPlayer(xfile2)
#player3 = OMXPlayer(xfile3)

# The player will initially be paused
player1.set_video_pos(0, 50, 500, 300)
player2.set_video_pos(0, 300, 500, 600)
player3.set_video_pos(0, 600, 500, 900)

#player1.play()
sleep(2)
#player1.pause()

player2.play()
sleep(2)
#player2.pause()

#player3.play()
sleep(2)
#player3.pause()

# Kill the `omxplayer` process gracefully.
#player1.quit()
#player2.quit()
#player3.quit()
