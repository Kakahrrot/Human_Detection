import cv2
from imutils.object_detection import non_max_suppression
import numpy as np
import imutils

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FPS, 60)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
#print(cv2. __version__)
while(True):
	ret, frame = cap.read(0)
	# print("shape: ", frame.shape)
	frame = imutils.resize(frame, width = min(400, frame.shape[1]))
	# orig = frame.copy()
	# rects, weights = hog.detectMultiScale(frame, winStride = (4,4), padding = (8,8), scale = 1.05)
	rects, weights = hog.detectMultiScale(frame, winStride = (4,4), padding = (8,8), scale = 10)
	# for x, y, w, h in rects:
		# cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)
	rects = np.array([[x, y, x + w, y + h] for x, y, w, h in rects])
	pick = non_max_suppression(rects, probs = None, overlapThresh = 0.15)
	for xa, ya, xb, yb in pick:
		print(yb - ya)
		cv2.rectangle(frame, (xa, ya), (xb, yb), (0,255, 0), 5)
	# frame = cv2.resize(frame, (1920, 1080), interpolation = cv2.INTER_CUBIC)
	cv2.imshow('frame', frame)
	# cv2.imshow('orig', orig)


	# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	# font = cv2.FONT_HERSHEY_SIMPLEX
	# cv2.putText(gray, 'Hello World', (150,150), font, 1, (255, 0, 0), 5, cv2.LINE_AA)
	
	# gray = cv2.GaussianBlur(gray, (5, 5), 0)
	# edged = cv2.Canny(gray, 35, 125)

	# cv2.imshow("edged", edged)
	# cnts = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	# cnts = imutils.grab_contours(cnts)
	# print("cnts: ", type(cnts))
	# c = max(cnts, key = cv2.contourArea)
	# print("c: ", type(c))

	# cv2.imshow('gray', edged)
	# 若按下 q 鍵則離開迴圈
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# 釋放攝影機
cap.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()