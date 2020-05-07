import cv2


haar_cascade_face = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
haar_cascade_eye = cv2.CascadeClassifier("haarcascade_eye.xml")

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = haar_cascade_face.detectMultiScale(gray, 1.2, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x + w, y + h), (255, 0, 0), 3)
        roi_gray = gray[y : y + h, x : x + h]
        roi_color = frame[y : y + h, x : x + h]
        eyes = haar_cascade_eye.detectMultiScale(roi_gray,1.1, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex + ew, ey + eh), (255, 0, 0), 3)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, "Human", (x, y), font, 1, (0, 255, 0), 2)
    cv2.imshow("face detection", frame)
    if(cv2.waitKey(1) & 0xff == ord("q")):
        break
cap.release()
cv2.destroyAllWindows()
