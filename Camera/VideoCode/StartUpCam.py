
# allow the camera to warmup, 
#frame motion counter
print "[INFO] warming up..."
time.sleep(conf["camera_warmup_time"])
avg = None
lastUploaded = datetime.datetime.now()
motionCounter = 0
print('[INFO] talking raspi started !!')