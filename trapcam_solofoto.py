import time
import os
import RPi.GPIO as GPIO

work_path = '/home/pi/Trapcam/data'

# Define a function to use each time the sensor is triggered
def photo():
    cmd="raspistill -o /home/pi/Trapcam/data/image"+str(i)+".jpg"
    os.system(cmd)
    return

# Set up the GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# For the first 10 triggers on pin 10
if os.listdir(work_path)==[]:
	for i in range(10):
		# At the moment it is triggered (voltage on pin 10 rising to 3v)...
		GPIO.wait_for_edge(10,GPIO.RISING)
		# ... use the function photo() to take a video/photo
		photo()

GPIO.cleanup()
