from time import sleep
import os
import RPi.GPIO as GPIO
from datetime import datetime, time

work_path = '/home/trapcam/TrapCam/data'
SENSOR_PIN = 17
IR_LED_PIN = 10 
SLEEP_TIME = 1 # seconds to wait before retrying
VIDEO_SECONDS = 10 # seconds of video duration
INITIAL_TRY = True

# Define the start and end times
start_time = time(0, 0, 0)  
end_time = time(10, 0, 0)   

# Define a function to use each time the sensor is triggered
def video(duration):
    # First capture a quick video of the scene
    cmd=f"libcamera-vid -o {work_path}/video"+str(datetime.now()).replace(" ","_")+f".h264 -t {duration*1000} --width 1640 --height 1232"
    os.system(cmd)
    return

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print('STARTING...')

#initial try
if INITIAL_TRY:
    while not GPIO.input(SENSOR_PIN):
        sleep(1)
        print('waiting for input...')
    cmd0=f'libcamera-still -t 1 -o {work_path}/test.jpg'
    os.system(cmd0)

#  main loop
while True:
    # Get the current time
    if start_time <= datetime.now().time() <= end_time and GPIO.input(SENSOR_PIN):
        # At the moment it is triggered (voltage on pin SENSOR_PIN rising) take video
        video(VIDEO_SECONDS)
    elif datetime.now().time() > end_time:
        break
    else:
        print('sensor is off...')
        sleep(SLEEP_TIME)

GPIO.cleanup() 

