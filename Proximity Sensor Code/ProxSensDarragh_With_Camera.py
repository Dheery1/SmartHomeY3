#Libraries
import RPi.GPIO as GPIO
import time

from picamera import PiCamera
from datetime import datetime
import os

camera = PiCamera()
today = datetime.now()
x = int(input('Enter value:'))


if today.hour < 12:
    h = "00"
else:
    h = "12"
    
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 23
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            
            if dist < 5.00:
                z = today.strftime('%Y %m %d ')+ h
                print(z)
                camera.start_preview(alpha=200)
                os.mkdir('/home/pi/Downloads/SmartHome-ProjectYear3--master/CameraCode/Photo/%s'%z)

                for i in range(x):
                    time.sleep(5)
                    camera.capture('/home/pi/Downloads/SmartHome-ProjectYear3--master/CameraCode/Photo/%s/image%i.jpg'%(z,i))
                camera.stop_preview()
                        
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
