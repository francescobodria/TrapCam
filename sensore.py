import time
import os
import RPi.GPIO as GPIO
#Programma per calibrare il sensore di movimento

PIN_NUMBER = 4
SLEEP_TIME = 1 #seconds
TIME_END = 200 #seconds to test

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_NUMBER, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

start = time.time()
print(start)

while(time.time()<start+TIME_END):
    if(GPIO.input(PIN_NUMBER)):
        print(f"Pin {PIN_NUMBER} is high")
    else:
        print(f"Pin {PIN_NUMBER} is low")
    time.sleep(SLEEP_TIME)
GPIO.cleanup()
