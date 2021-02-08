#!/usr/bin/python
#coding:utf-8

import time 
import RPi.GPIO as GPIO
import os

ch = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(ch,GPIO.IN,pull_up_down=GPIO.PUD_UP)

sw_status = 1

while True:
    GPIO.wait_for_edge(ch,GPIO.FALLING)
    sw_counter = 0

    while True:
        sw_status = GPIO.input(ch)
        if sw_status == 0:
            sw_counter = sw_counter + 1
            if sw_counter >= 200:
                print("The system is shutdown")
                time.sleep(1)
                os.system("sudo shutdown -h now")
                break
        else:
            print("If you want to shutdown the system, please keep pushing the button more than 2s.")
            break

        time.sleep(0.01)

GPIO.cleanup()
