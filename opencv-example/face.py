import cv2

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(0)


while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.5,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Human", (x+10, y-10),
                    cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('FaceDetection', frame)

    # Keyboard input
    k = cv2.waitKey(1)
    if k % 256 == 27:  # ESC Pressed
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()