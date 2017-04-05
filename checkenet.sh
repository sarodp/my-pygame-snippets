#!/bin/bash

check_url () {
  if [ "$2" == "ok" ]; then
     echo "ok"
  fi

  if [ "$2" != "ok" ]
  then
    res=$(curl -w %{http_code} -s --output /dev/null $1)
    if [ $res -ne 200 ] && [ $res -ne 301 ] && [ $res -ne 302 ]
    then
        echo "error"
    else
        echo "ok"
    fi
  fi 
}

status=$(check_url "http://google.com" "")
echo "check_url=" $status

if [ "$status" != "ok" ]; then
    echo "ethernet error"
    #sudo halt
fi

