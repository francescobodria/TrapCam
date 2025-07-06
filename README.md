# TrapCam
Trapcam made easy with raspberry pi, 

Requirement: picamera/picamera noir and a proximity sensor

The main usage is:
	1) modify time to wait before start capturing and pin number of the sensor in trapcam.py
	2) launch python trapcam.py in a screen terminal
	3) walk away
The program will take a short video if the sensor is triggered 

Now let's describe files and directories:

trapcam.py: main file

trapcam_it.py: version with ir led

test_sensore.py: launch to debug the sensor, useful for tries.

test_ir_camera.py: test the ir led and the camera

./data: directory in which save images and videos

scrip_trap_cam: some script useful for rasperrypi
	eliminarefoto:		delete data file and recreate empy folder
	montarechiavetta:	mount usb
	scaricafoto:		copy data in usb
	smontarechiavetta:	unmount usb
	test:				take a photo and a short video, useful to check the camera view
	hotspot:			create a network called TrapCam to connect to 

## Setup new board

install raspbian lite with installer

```bash
sudo apt update
sudo apt install vim
sudo apt install screen
sudo apt install git

git clone https://github.com/francescobodria/TrapCam

screen -S trapcam

python trapcam.py
```