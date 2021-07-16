import cv2
import sys
import time
import frame


box = frame.HDFrame((0, 0), (80 * 2, 25 * 2))
fileid = 0

if len(sys.argv) > 1:
	fileid = sys.argv[1]

cap = cv2.VideoCapture(fileid)

while True:
	_, data = cap.read()
	box.draw(data)
	time.sleep(0.0)
