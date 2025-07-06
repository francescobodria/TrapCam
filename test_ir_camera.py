# import RPi.GPIO as GPIO
import time
import os
from gpiozero import PWMOutputDevice, DigitalOutputDevice

def flash_ir(duration=0.5):
    """Flash the IR LEDs for a set duration (in seconds)."""
    ir = DigitalOutputDevice(GPIO_PIN)
    ir.on()
    time.sleep(duration)
    ir.off()

def constant_ir():
    """Turn the IR LEDs on constantly."""
    ir = DigitalOutputDevice(GPIO_PIN)
    ir.on()
    input("Press Enter to turn off the IR light...")
    ir.off()

def pwm_ir():
    """Control brightness using PWM (0.0 to 1.0)."""
    ir = PWMOutputDevice(GPIO_PIN)
    try:
        while True:
            level = float(input("Enter brightness (0.0 to 1.0): "))
            if 0.0 <= level <= 1.0:
                ir.value = level
            else:
                print("Invalid range.")
    except KeyboardInterrupt:
        ir.value = 0


print('IR LED on')
ir = DigitalOutputDevice(10)
ir.on()

time.sleep(1)
print('Capturing photo...')
os.system("libcamera-still -o ./test_ir.jpg -t 1")
print('Capturing video...')
os.system(f'libcamera-vid -o test_ir.h264 -t 5000 --width 1640 --height 1232')
time.sleep(1)

ir.off()
print('IR LED off')
