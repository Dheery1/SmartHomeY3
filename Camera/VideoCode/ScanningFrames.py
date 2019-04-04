# capture frames from the camera
for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image and initialize
	# the timestamp and occupied/unoccupied text
	frame = f.array
	timestamp = datetime.datetime.now()
	text = "Unoccupied"

	######################################################################
	# COMPUTER VISION
	######################################################################
	# resize the frame, convert it to grayscale, and blur it
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, tuple(conf['blur_size']), 0)
	
	# if the average frame is None, initialize it
	if avg is None:
		print "[INFO] starting background model..."
		avg = gray.copy().astype("float")
		rawCapture.truncate(0)
		continue

	# accumulate the weighted average between the current frame and
	# previous frames, then compute the difference between the current
	# frame and running average
	frameDelta = cv2.absdiff(gray, cv2.convertScaleAbs(avg))
	cv2.accumulateWeighted(gray, avg, 0.5)