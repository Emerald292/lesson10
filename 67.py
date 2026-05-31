import cv2

image_path = '52.png'

cate_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image = cv2.imread(image_path)

cate_face = cate_face_cascade.detectMultiScale(image)

print(cate_face)

for (x, y, w, h) in cate_face:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 3)

cv2.imshow("Cat", image)
cv2.waitKey()