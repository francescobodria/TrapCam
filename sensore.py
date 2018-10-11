import time
import os
import RPi.GPIO as GPIO
#Programma per calibrare il sensore di movimento

# Set up the GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

start = time.time()
print(start)

while(time.time()<start+200):
    if(GPIO.input(10)):
        print("Pin 10 is high")
    else:
        print("Pin 10 is low")
    time.sleep(1)
GPIO.cleanup()
