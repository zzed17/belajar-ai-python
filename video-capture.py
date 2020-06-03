import cv2
cap = cv2.VideoCapture(4)

while(True):
    ret,frame = cap.read()
    cv2.imshow("Gambar",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cap.release()