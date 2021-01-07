import cv2

plateCascade = cv2.CascadeClassifier('resources/haarcascade_russian_plate_number.xml')
minArea = 500
color = (255, 0, 255)

widthImg = 480
heightImg = 640

vid = cv2.VideoCapture(0)

vid.set(3, widthImg)
vid.set(4, heightImg)
vid.set(10, 150)

count = 0
while True:
    success, img = vid.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numberPlates = plateCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in numberPlates:
        area = w * h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.putText(img, 'Number Plate', (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            imgRoi = img[y:y + h, x:x + w]
            cv2.imshow('ROI', imgRoi)

    cv2.imshow('Result', img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('resources/scanned/plate_' + str(count) + '.jpg', imgRoi)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, 'Scan Saved', (150, 265), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255), 2)
        cv2.imshow('Result', img)
        cv2.waitKey(500)
        count += 1
