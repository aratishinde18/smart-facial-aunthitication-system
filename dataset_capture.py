swatiimport cv2
import os

name = input("Enter name: ")

cam = cv2.VideoCapture(0)

count = 0

while True:
    ret, frame = cam.read()

    cv2.imshow("Camera", frame)

    cv2.imwrite(f"dataset/{name}_{count}.jpg", frame)

    count += 1

    if count == 20:
        break

    cv2.waitKey(200)

cam.release()
cv2.destroyAllWindows()

print("Dataset ready")