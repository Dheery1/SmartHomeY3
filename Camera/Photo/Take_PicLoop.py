from picamera import PiCamera
from time import sleep
from datetime import datetime
import os

camera = PiCamera()
today = datetime.now()
x = int(input('Enter value:'))

if today.hour < 12:
    h = "00"
else:
    h = "12"
    
z = today.strftime('%Y %m %d ')+ h
print(z)
camera.start_preview(alpha=200)
os.mkdir('/home/pi/Downloads/SmartHome-ProjectYear3--master/CameraCode/Photo/%s'%z)


for i in range(x):
    sleep(5)
    camera.capture('/home/pi/Downloads/SmartHome-ProjectYear3--master/CameraCode/Photo/%s/image%i.jpg'%(z,i))
camera.stop_preview()
camera.close()

