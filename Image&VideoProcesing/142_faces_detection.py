import cv2

face_cascade = cv2.CascadeClassifier("/Image&VideoProcesing/images/faces/haarcascade_frontalface_default.xml")

img = cv2.imread("/Image&VideoProcesing/images/faces/photo.jpg")

cv2.imshow("Gray",img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05)

cv2.imshow("Gray", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


