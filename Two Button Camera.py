# Author: Matthew Baker
# GitHub: https://github.com/mbaker92

# omxplayer filename

from picamera import PiCamera
from time import sleep
import RPi.GPIO as gpio
import datetime

gpio.setmode(gpio.BCM)

#Buttons Connected to GPIO Pins 17 and 18
gpio.setup(17, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(18, gpio.IN, pull_up_down=gpio.PUD_UP)

# Initialize Camera and Set Exposure Mode
camera= PiCamera()
camera.exposure_mode = 'antishake'

#Ctrl + c in Terminal to Get Out of Infinite Loop	
while True:
	
	#Get values from button presses
	inputVideo = gpio.input(17)
	inputCamera = gpio.input(18)

	# If the Video Button is Pressed, Record for Ten Seconds and Save File With Current Date and Time
	if inputVideo == False:
		print('Video Button Pressed')
		camera.start_recording('/home/pi/Documents/' +  datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S') + '.h264')
		sleep(10)
		camera.stop_recording()
		sleep(.2)
		print('Video Capture Done')

	# If The Camera Button is Pressed Take a Photo and Save With Current Date and Time
	if inputCamera == False:
		print('Camera Button Pressed')
		camera.capture('/home/pi/Documents/' +  datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S') + '.png')
		sleep(.2)


