
from ultralytics import YOLO
import cv2
import mediapipe as mp

model = YOLO("/Users/millatina/Documents/MU/Portfolio AI/Hand_Sign_Detection/best.pt")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(frame, verbose=False)  # verbose=False for cleaner output
    annotated_frame = results[0].plot()
    cv2.imshow("YOLO Hand Sign Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 