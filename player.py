import cv2
import sys

cap = cv2.VideoCapture('udp://192.168.0.147:1234',cv2.CAP_FFMPEG)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 3)

while True:
        ret, frame = cap.read()

        if not ret:
                print('frame empty')
                break

        cv2.imshow('image', frame)

        # Press "q" to exit from the player window
        if cv2.waitKey(1)&0XFF == ord('q'):
                break

cap.release()
cv2.destroyAllWindows()
