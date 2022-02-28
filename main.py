import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
image = cv2.imread('mitlesh.jpg')
from matplotlib import pyplot as plt
plt.imshow(image)
RGB_img=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(RGB_img)
GR_img = cv2.cvtColor(RGB_img,cv2.COLOR_BGR2GRAY)
plt.imshow(GR_img)
faces=face_cascade.detectMultiScale(
    GR_img,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30,30)
)

print(faces)
image=cv2.imread("mitlesh.jpg")
for(x,y,w,h)in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),4)
RGB_img=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(RGB_img)
ims=[]
for(x,y,w,h) in faces:
    crop=RGB_img[y-30:y+h+2000,x-30:x+w+900]
    ims.append(crop)
plt.imshow(ims[0])

