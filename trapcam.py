import time
import os
import RPi.GPIO as GPIO

work_path = '/home/pi/Trapcam/data'
time_to_wait=60. #time to sleep before start in second
num_photo=5000 #max number of photo


# Define a function to use each time the sensor is triggered
def photo():
    # First capture a quick video of the scene
    cmd="raspivid -o /home/pi/Trapcam/data/video"+str(i)+".h264 -t 10000"
    os.system(cmd)
    time.sleep(1)
    j=1
    # While the trigger is still active (pin 10 at 3v)...
    while(GPIO.input(10)):
        # ... keep taking photos
        cmd="raspistill -o /home/pi/Trapcam/data/image"+str(i)+"_"+str(j)+".jpg"
        os.system(cmd)
        j=j+1
    return

# Set up the GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#initial try
if os.listdir(work_path)==[]:
	GPIO.wait_for_edge(10,GPIO.RISING)
	cmd0='raspistill -o /home/pi/Trapcam/prova.jpg'
	os.system(cmd0)
	time.sleep(time_to_wait)


# For the first x triggers on pin 10
if os.listdir(work_path)==[]:
    for i in range(num_photo):
        # At the moment it is triggered (voltage on pin 10 rising to 3v)...
        GPIO.wait_for_edge(10,GPIO.RISING)
        # ... use the function photo() to take a video/photo
        photo()

GPIO.cleanup() 
