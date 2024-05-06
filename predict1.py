import os
import cv2
import serial
from ultralytics import YOLO

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
H, W, _ = frame.shape

model_path = r"E:\Food calorie\CopiedImages\webcam\runs\detect\train3\yolov8s.pt"
model = YOLO(model_path)

threshold = 0.5

# Establish serial communication with Arduino
arduino = serial.Serial('COM18', 9600)  # Change 'COM3' to your Arduino's port

while ret:
    results = model(frame)[0]

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            detected_class = results.names[int(class_id)].upper()
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, detected_class, (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

            # Send data to Arduino based on detected class
            if detected_class == 'APPLE':
                arduino.write(b'A')  # Send 'A' for Apple
            elif detected_class == 'TOMATO':
                arduino.write(b'T')  # Send 'T' for Tomato

    cv2.imshow('Real-time Object Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    ret, frame = cap.read()

cap.release()
cv2.destroyAllWindows()
