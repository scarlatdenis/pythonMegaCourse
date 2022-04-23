from tabnanny import check
import cv2

video = cv2.VideoCapture(0)

a = 1

while True:
    a += 1
    check, frame = video.read()
    print(check)
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Capturing", gray)

    key = cv2.waitKey(100)  # frame loop rate

    if key == ord('q'):
        break
# when press q process will stoped
print(a) # fps
video.release()

cv2.destroyAllWindows()
