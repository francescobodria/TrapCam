import picamera
import os
import RPi.GPIO as GPIO
import time

GPIO.cleanup()

#set the GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

work_path = '/home/pi/Trapcam/data'
waiting_time=100

e=0

#se la directory work_path e' vuota fai partire il ciclo
if os.listdir(work_path)==[]:
	#cambio directory
	os.chdir(work_path)
	#settaggio fotocamera
	camera = picamera.PiCamera()
	#tempo iniziale
	start = time.time()
	#100 e' la durata
	while(time.time()<start+waiting_time):
    		if(GPIO.input(10)):   #se la variabile del pin e' vera
  			#impostazioni fotocamera
			camera.exposure_mode = 'auto'
			camera.meter_mode = 'average'
			camera.awb_mode = 'auto'
			camera.image_effect = 'none'
			camera.resolution = (1024, 768)
      			nomefile = 'image'+str(e)+'.jpg'
			camera.capture(nomefile)
			print("foto scattata")
			e=e+1
			print(e)
			time.sleep(1)
    		else:
        		print("niente da segnalare")
			time.sleep(1)
else : print 'error'

GPIO.cleanup()



