# Author: Matthew Baker
# GitHub: https://github.com/mbaker92

#omxplayer filename
#used on command line to play video

from picamera import PiCamera
from time import sleep
from gpiozero import Button, LED
import datetime

led = LED(18)
button = Button(17)
camera = PiCamera()

camera.exposure_mode = 'antishake'
button.wait_for_press()
camera.start_recording('/home/pi/Documents/Video/' + datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S') +'.h264')
led.on()
sleep(10)
camera.stop_recording()
led.off()