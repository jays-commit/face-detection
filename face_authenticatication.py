import face_recognition
import os
import cv2
import time
import sys


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

# code above is a simpler way but the ds.store file stops code from working
for name in os.listdir(KNOWN_FACES_DIR):
    dir_path = os.path.join(KNOWN_FACES_DIR, name)
    # if it's a directory
    if os.path.isdir(dir_path):
        for filename in os.listdir(dir_path):
            # if the file is a valid file (a better way could be to check your specific extension, e.g., png)
            if not filename.startswith('.'):
                filepath = os.path.join(dir_path, filename)
                image = face_recognition.load_image_file(filepath)

        # Load an image
        image = face_recognition.load_image_file(f"{KNOWN_FACES_DIR}/{name}/{filename}")

        # Get 128-dimension face encoding
        # Always returns a list of found faces, for this purpose we take first face only
        # (assuming one face per image as you can't be twice on one image)
        encoding = face_recognition.face_encodings(image)[0]

        # Append encodings and name
        known_faces.append(encoding)
        known_names.append(name)


print("Verifying Identity....")
while True:
    ret, image = video.read()

    # for filename in os.listdir(UNKNOWN_FACES_DIR):
    # print(filename)
    # image = face_recognition.load_image_file(f"{UNKNOWN_FACES_DIR}/{filename}")

    # Twe first grab face locations - we'll need them to draw boxes
    locations = face_recognition.face_locations(image, model=MODEL)

    # Now since we know locations, we can pass them to face_encodings as second argument
    # Without that it will search for faces once again slowing down whole process
    encoding = face_recognition.face_encodings(image, locations)

    # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # we assume that there might be more faces in an image - we can find faces of different people
    for face_encoding, face_locations in zip(encoding, locations):

        # We use compare_faces (but might use face_distance as well)
        # Returns array of True/False values in order of passed known_faces
        results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
        match = None
        if True in results: # If at least one is true, get a name of first of found labels
            match = known_names[results.index(True)]

            time.sleep(8)
            print(f"Match Found: {match}")
            print("User Authenticated")
            sys.exit()
        else:
            print("Match not found\n User authentication denied")
            time.sleep(5)
            sys.exit()




        # Each location contains positions in order: top, right, bottom, left
        top_left = (face_locations[3], face_locations[0])
        bottom_right = (face_locations[1], face_locations[2])
        color = [0, 255, 0]

        # Paint frame
        cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)

        # Now we need smaller, filled grame below for a name
        # This time we use bottom in both corners - to start from bottom and move 50 pixels down
        top_left = (face_locations[3], face_locations[2])
        bottom_right = (face_locations[1], face_locations[2] + 22)
        cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)

        # Write a name
        cv2.putText(image, match, (face_locations[3] + 10, face_locations[2] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (200, 200, 200), FONT_THICKNESS)

    # Show webcam vid
    cv2.imshow(filename, image)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
video.release()
cv2.destroyAllWindows()
