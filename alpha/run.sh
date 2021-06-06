#!/bin/bash

while true
do
    fileName=$(inotifywait -r -e create /home/olek/alpha/files | sed -r 's/^.*CREATE(,ISDIR)*\s+(.*)$/\2/g')
    /home/olek/alpha/observer.sh
done