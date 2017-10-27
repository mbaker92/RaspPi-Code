# Author: Matthew Baker
# GitHub: https://github.com/mbaker92

# Libraries 
from gpiozero import MotionSensor
from picamera import PiCamera
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import datetime
import smtplib
import time

# Email Addresses
fromAddr = 'Address Sending Email'
toAddr = 'Address Receiving Email'

#Motion Sensor and Camera Initialized
PIRSensor = MotionSensor(4)
camera = PiCamera()

# Variable to Exit while loop
Tripped = True

#wait five seconds
time.sleep(5)

while Tripped:
	if PIRSensor.motion_detected:
		print("Motion Detected")

		#Sent Tripped to False and capture picture
		Tripped = False
		timeCaptured = '/home/pi/Desktop' + datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S') + '.png'
		camera.rotation = 180
		camera.capture(timeCaptured)
		
		print("Image Captured")


		#Create the Message
		msg = MIMEMultipart()
		msg[ 'Subject'] = 'Intruder'
		msg['From'] = fromAddr
		msg['To'] = toAddr

		#Attach the file
		File = open(timeCaptured, 'rb')
		img = MIMEImage(File.read())
		File.close()
		msg.attach(img)

	 	# Credentials for fromAddr
	        username = 'Email Address'
	        password = 'Password'

	        # The actual mail send from a microsoft account
	        server = smtplib.SMTP('smtp-mail.outlook.com:587')
	        server.starttls()
	        server.login(username,password)
	        server.sendmail(fromAddr, toAddr, msg.as_string())
	        server.quit()

		print("Email Sent")

