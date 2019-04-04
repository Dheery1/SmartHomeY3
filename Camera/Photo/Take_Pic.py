from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview(alpha=200)
sleep(5)
camera.capture('/home/pi/Downloads/SmartHome-ProjectYear3--master/CameraCode/Photo/image.jpg')
camera.stop_preview()
