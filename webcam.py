import cv2

video = cv2.VideoCapture(0)
sub = cv2.createBackgroundSubtractorMOG2(25, 50)

while True:

    ret, frame = video.read()

    if ret:
        mask = sub.apply(frame)
        cv2.imshow('Mask', mask)

        if cv2.waitKey(5) == ord('X'):
            break



cv2.destroyAllWindows()
video.release()