#!/bin/bash
#scarica tutti i file presenti nella directory Photo su una chiavetta

zip -r picamera /home/pi/Trapcam/data
mv picamera.zip /var/tmp/chiavetta
