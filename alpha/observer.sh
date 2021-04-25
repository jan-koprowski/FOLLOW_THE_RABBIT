#!/bin/bash
# coding=utf-8

MYPATH='/Users/olek/Documents/follow-the-rabbit/alpha/files'
LATEST=$(ls -t $MYPATH | head -1)

echo $LATEST >> observer.txt  
# obsertver is file to debug the process


python read_file.py $LATEST



# Skrypt do monitorowania zmiany w folderze - wersja macos:
# fswatch -o /Users/olek/Documents/follow-the-rabbit/alpha/files | xargs -n1 -I{} /Users/olek/Documents/follow-the-rabbit/alpha/observer.sh
# Odpowiednikiem linuxowym jest inotifywait