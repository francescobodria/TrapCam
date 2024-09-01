#!/bin/bash
#scatta una foto nella directory corrente
libcamera-still -o test.jpg --nopreview

# fa un piccolo video nella directory corrente
libcamera-vid -o test.h264 --nopreview
