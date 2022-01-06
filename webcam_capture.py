import cv2
import time

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    faces = face_cascade.detectMultiScale(frame,
                                          scaleFactor=1.05,
                                          minNeighbors=5,



                                          )
    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        print(faces)

    cv2.imshow("Selfie", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break


video.release()
cv2.destroyAllWindows()

#
# import cv2
# import time
#
# # number determines on how many cams your pc has
# # you can use a video file too by putting the name
# video = cv2.VideoCapture(0)
#
# a= 1
# while True:
#     a += 1
#     check, frame = video.read()
#
#     print(check)
#     print(frame)
#
#     # time.sleep(5)
#     cv2.imshow("capture", frame)
#     key =cv2.waitKey(1)
#
#     if key == ord("q"):
#         break
#
#
# print(a)
#
#
#
# video.release()
# cv2.destroyAllWindows()
