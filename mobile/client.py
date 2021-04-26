#!/usr/bin/python
# -*- coding: utf-8 -*- 
import random as rand
import time
import os


# connection info
ALPHA_NAME = "olek"
APLHA_IP = "192.168.18.66"

COMBINATIONS = 1000

MY_TIME = str(time.ctime()).replace(' ', '-')

def create_file():
    # zmienić num na liczbę przeporowadzonych operacji
    open_line = MY_TIME
    create_file = 'echo \"' + open_line + '\" >> files/' + MY_TIME
    os.system(create_file)

def add_position_info():
    for x in range(0,COMBINATIONS):
        try:
            i = rand.randint(1,8)
            add_rand = 'echo \"' + str(i) + '\" >> files/' + MY_TIME 
            os.system(add_rand)
        except :
            print('Except')


def connect():
    create_file()
    add_position_info()
    # pamietać na urządzeniu mobilnym o zmianie ściezek dostepowych (by ja sprawdzic - pwd)
    my_cmd = 'scp /Users/olek/Documents/follow-the-rabbit/mobile/files/'+ MY_TIME +' '+ ALPHA_NAME +'@'+ APLHA_IP +':/home/olek/Alpha/files'
    os.system(my_cmd)

connect()