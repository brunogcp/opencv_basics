import cv2

img = cv2.imread('resources/unit.PNG')
print(img.shape)

imgResized = cv2.resize(img, (500, 100))
print(imgResized.shape)

imgCropped = img[0:100, 100:200]

cv2.imshow('Image', img)
cv2.imshow('Image Resized', imgResized)
cv2.imshow('Image Cropped', imgCropped)

cv2.waitKey(0)
