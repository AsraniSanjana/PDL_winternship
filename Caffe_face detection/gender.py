import cv2
import numpy as np

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load pre-trained gender classification model
gender_model = cv2.dnn.readNetFromCaffe('gender_deploy.prototxt', 'gender_net.caffemodel')

cap = cv2.VideoCapture('people2.mp4')


while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Iterate through detected faces
    for (x, y, w, h) in faces:
        # Draw rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Crop the face for gender classification
        face_crop = frame[y:y+h, x:x+w]

        # Preprocess the face for gender classification
        blob = cv2.dnn.blobFromImage(face_crop, scalefactor=1.0, size=(227, 227), mean=(78.4263377603, 87.7689143744, 114.895847746), swapRB=False)

        # Set the input to the gender model and forward pass
        gender_model.setInput(blob)
        gender_preds = gender_model.forward()

        # Get the gender label
        gender = 'Female' if gender_preds[0][0] > gender_preds[0][1] else 'Male'
        confidence = max(gender_preds[0])

        # Display the gender on the frame
        gender_label = f"{gender} ({confidence:.2f})"
        cv2.putText(frame, gender_label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('img', frame)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()
