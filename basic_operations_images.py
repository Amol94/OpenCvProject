import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

print(img.shape)# return a tuple of number of rows,columns and channels
print(img.size)#return total number of pixels is accessed
print(img.dtype)#return Image datatype is obtained

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

ball = img[280:340, 330:390]  #co-ordinates of the ball
img[273:333, 100:160] = ball #placing ball on different co-ordinate

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))
#dst = cv2.add(img, img2) #add two images if the size of image is same else it produce error
# or
dst = cv2.addWeighted(img, .9, img2, .1, 0) #.9 and .1 is weight
cv2.imshow('image', dst)
#cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()