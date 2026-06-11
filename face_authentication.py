import cv2
import os

dataset_path = "dataset"

known_faces = []
known_names = []

for file in os.listdir(dataset_path):
    img = cv2.imread(os.path.join(dataset_path, file), 0)
    known_faces.append(img)
    name = file.split("_")[0]
    known_names.append(name)

cam = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                     "haarcascade_frontalface_default.xml")

while True:
    ret, frame = cam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    label = "Unauthorized"
    access = "Access Denied"

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]

        for i, known_face in enumerate(known_faces):
            known_face = cv2.resize(known_face, (w, h))

            diff = cv2.absdiff(face, known_face)
            score = diff.mean()

            if score < 50:
                label = known_names[i]
                access = "Access Granted"

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(frame, label, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

        cv2.putText(frame, access, (x, y+h+30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,255), 2)

    cv2.imshow("Smart Facial Authentication", frame)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()