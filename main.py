# import libraries
import cv2
import face_recognition
import datetime

# Get a reference to webcam
video_capture = cv2.VideoCapture("/Users/ayushdeb/Downloads/dataset1/Video_clip/jkl.mp4")

# Initialize variables
face_locations = []
i=0

import os

directory = r'/Users/ayushdeb/Desktop/images'
directorys = r'/Users/ayushdeb/Desktop/faces'



while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)

    # Display the results
    for top, right, bottom, left in face_locations:
        # Draw a box around the face
        img = cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # bottom =bottom+100
    # left = left + 100
    print(bottom,left)


    if ret:
        face = img[top:bottom, left:right]
        # imgs =cv2.imshow("Cropped Face", face)
        dt = str(datetime.datetime.now())
        print(dt)
        os.chdir(directory)
        print(os.listdir(directory))
        filename = 'Frame' + str(i) + '.jpg'
        cv2.imwrite(filename, img)

        # os.chdir(directorys)
        # print(os.listdir(directorys))
        filenames = 'Face' + str(i) + '.jpg'
        cv2.imwrite('/Users/ayushdeb/Desktop/fec/'+filenames, face)

        i += 30
        video_capture .set(cv2.CAP_PROP_POS_FRAMES, i)
        if (i>=4410):
            break




    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break# import libraries

video_capture.release()
cv2.destroyAllWindows()