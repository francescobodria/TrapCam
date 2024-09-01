import time
import os
import RPi.GPIO as GPIO
from datetime import datetime, time

work_path = '/home/pi/TrapCam/data'
SENSOR_PIN = 4
SLEEP_TIME = 1 # seconds to wait before retrying
VIDEO_SECONDS = 10 # seconds of video duration

# Define the start and end times
start_time = time(5, 0, 0)  # 8:00 AM
end_time = time(10, 0, 0)   # 10:00 AM

# Define a function to use each time the sensor is triggered
def video(duration):
    # First capture a quick video of the scene
    cmd=f"libcamera-vid -o {work_path}/video"+str(datetime.now()).replace(" ","_")+f".h264 -t {duration*1000}"
    os.system(cmd)
    return

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#initial try
while not GPIO.input(SENSOR_PIN):
    time.sleep(1)
cmd0=f'libcamera-still -t 1 -o {work_path}/test.jpg'
os.system(cmd0)

#  main loop
while True:
    # Get the current time
    if start_time <= datetime.now().time() <= end_time and GPIO.input(SENSOR_PIN):
        # At the moment it is triggered (voltage on pin 10 rising to 3v) take video
        video(VIDEO_SECONDS)
    elif datetime.now().time() > end_time:
        break
    else:
        time.sleep(SLEEP_TIME)

GPIO.cleanup() 
