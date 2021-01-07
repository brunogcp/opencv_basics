import cv2

print('Package Imported')

# Image Capture
# img = cv2.imread('resources/unit.PNG')
#
# cv2.imshow('Output', img)
# cv2.waitKey(0)

# Video Capture
# vid = cv2.VideoCapture('resources/robot.mp4')
#
# while True:
#     success, img = vid.read()
#     cv2.imshow('Video', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# WebCam Capture
vid = cv2.VideoCapture(0)
vid.set(3, 640)
vid.set(4, 480)
vid.set(10, 100)

while True:
    success, img = vid.read()
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
