# TrapCam
Trapcam made easy with raspberry pi, 

Requirement: picamera and a proximity sensor

The main usage is:
	1) modify time to wait before start capturing and pin number of the sensor in trapcam.py
	2) run eliminarefoto to delete the folder data this is because the program doesn't work if there are videos in the data folder
	3) launch python trapcam.py in terminal
	4) walk away
The program will take a short video if the sensor is triggered 

Now let's describe files and directories:

trapcam.py: main file

trapcam_solofoto: is equal to the main file but it takes only photo and not video

trapcam_pythoncam: use pythoncam lib

sensore.py: launch to debug the sensor, useful for tries.

data: directory in which save images and videos

scrip_trap_cam: some script useful for rasperrypi
	eliminarefoto:		delete data file and recreate empy folder
	montarechiavetta:	mount usb
	scaricafoto:		copy data in usb
	smontarechiavetta:	unmount usb
	test:				take a photo and a short video, useful to check the camera view
