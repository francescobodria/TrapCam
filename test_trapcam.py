import time
import os
import RPi.GPIO as GPIO
from datetime import datetime

work_path = '/home/pi/TrapCam/data'
SENSOR_PIN = 4
SLEEP_TIME = 1 # test ever SLEEP_TIME seconds
TRIGGER_NBR = 10 # number of tests 

# Define a function to use each time the sensor is triggered
def video():
    cmd=f"libcamera-vid -t 10000 -o {work_path}/video_test_"+str(datetime.now()).replace(" ","_")+".h264"
    os.system(cmd)
    return

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# For the first 10 triggers on pin SENSOR_PIN
for i in range(TRIGGER_NBR):
    # At the moment it is triggered (voltage on pin SENSOR_PIN rising)
    level = GPIO.input(SENSOR_PIN)
    if level:
        # ... use the function photo() to take a video/photo
        video()
    else:
        time.sleep(SLEEP_TIME)

GPIO.cleanup()
