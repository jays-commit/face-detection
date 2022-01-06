import face_recognition
import os
import cv2
import time
import sys

# test
KNOWN_FACES_DIR = "known_faces"
# UNKNOWN_FACES_DIR = "unknown_faces"
TOLERANCE = 0.8
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = "hog"

# username = input("Enter Username")
# if username == authentication.login:
#     print("success")
# else:
#     print("access denied")

video = cv2.VideoCapture(0)

print("loading known faces....")

known_faces = []
known_names = []

# for name in os.listdir(KNOWN_FACES_DIR):
#     for filename in os.listdir(f"{KNOWN_FACES_DIR}/{name}"):

for name in os.listdir(KNOWN_FACES_DIR):
    dir_path = os.path.join(KNOWN_FACES_DIR, name)
    # if it's a directory
    if os.path.isdir(dir_path):
        for filename in os.listdir(dir_path):
            # if the file is a valid file (a better way could be to check your specific extension, e.g., png)
            if not filename.startswith('.'):
                filepath = os.path.join(dir_path, filename)
                image = face_recognition.load_image_file(filepath)

        image = face_recognition.load_image_file(f"{KNOWN_FACES_DIR}/{name}/{filename}")

        encoding = face_recognition.face_encodings(image)[0]

        known_faces.append(encoding)
        known_names.append(name)

# Test
print("Verifying Identity....")
while True:
    ret, image = video.read()
    # for filename in os.listdir(UNKNOWN_FACES_DIR):
    # print(filename)
    # image = face_recognition.load_image_file(f"{UNKNOWN_FACES_DIR}/{filename}")
    locations = face_recognition.face_locations(image, model=MODEL)
    encoding = face_recognition.face_encodings(image, locations)
    # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    for face_encoding, face_locations in zip(encoding, locations):
        results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
        match = None
        if True in results:
            match = known_names[results.index(True)]

            time.sleep(8)
            print(f"Match Found: {match}")
            print("User Authenticated")
            sys.exit()
        else:
            print("Match not found\n User authenitication denied")
            time.sleep(5)
            sys.exit()

            # print("processing credentials")
            # time.sleep(10)
            # print("access granted")
            # sys.exit()

        top_left = (face_locations[3], face_locations[0])
        bottom_right = (face_locations[1], face_locations[2])
        color = [0, 255, 0]
        cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)

        top_left = (face_locations[3], face_locations[2])
        bottom_right = (face_locations[1], face_locations[2] + 22)
        cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
        cv2.putText(image, match, (face_locations[3] + 10, face_locations[2] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (200, 200, 200), FONT_THICKNESS)

    cv2.imshow(filename, image)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
video.release()
cv2.destroyAllWindows()
