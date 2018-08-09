import numpy.core.multiarray
import cv2
import numpy as np

ball_cas = cv2.CascadeClassifier('cascade.xml')
cap = cv2.VideoCapture(1)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    balls = ball_cas.detectMultiScale(gray)

    for (x,y,w,h) in balls:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'Ball', (x-w, y-h), font, 0.5, (0,255,0), 2, cv2.LINE_AA)
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        cv2.imshow('img', img)
    cv2.imshow('img', img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
        

cap.release()
cv2.destroyAllWindows()
