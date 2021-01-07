import cv2
import numpy as np

frameWidth = 640
frameHeight = 480

vid = cv2.VideoCapture(0)

vid.set(3, frameWidth)
vid.set(4, frameHeight)
vid.set(10, 150)

myColors = [[3, 22, 135, 237, 125, 182],
            [30, 73, 116, 235, 111, 210],
            [1, 6, 104, 197, 127, 235],
            [98, 112, 126, 204, 156, 239],
            [25, 36, 146, 230, 139, 219],
            [0, 5, 141, 200, 0, 255]]

myColorsValues = [[51, 153, 255],
                  [0, 255, 0],
                  [0, 0, 255],
                  [255, 0, 0],
                  [0, 255, 255],
                  [0, 51, 255]]

myPoints = []


def find_color(img, myColors, myColorsValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        l = [color[0], color[2], color[4]]
        u = [color[1], color[3], color[5]]
        lower = np.array(l)
        upper = np.array(u)
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = get_contours(mask)
        cv2.circle(imgResult, (x, y), 10, myColorsValues[count], cv2.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
        count += 1
        # cv2.imshow(str(color[0]), mask)
    return newPoints


def get_contours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = (0, 0, 0, 0)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(imgResult, cnt, -1, (255, 200, 100), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w // 2, y


def draw_on_canvas(myPoints, myColorsValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorsValues[point[2]], cv2.FILLED)


while True:
    success, img = vid.read()
    imgResult = img.copy()
    newPoints = find_color(img, myColors, myColorsValues)
    if len(newPoints) != 0:
        for newPoint in newPoints:
            myPoints.append(newPoint)
    if len(myPoints) != 0:
        draw_on_canvas(myPoints, myColorsValues)
    cv2.imshow('Video', imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
