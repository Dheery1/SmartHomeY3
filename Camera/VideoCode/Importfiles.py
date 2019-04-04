from picamera.array import PiRGBArray
from picamera import PiCamera
from utils import send_email, TempImage
import argparse
import warnings
import datetime
import json
import time
import cv2

# load some config
conf = json.load(open(args["conf"]))

# initialize the camera 
camera = PiCamera()
camera.resolution = tuple(conf["resolution"])
camera.framerate = conf["fps"]
rawCapture = PiRGBArray(camera, size=tuple(conf["resolution"]))