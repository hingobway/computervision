import cv2 as cv

cap = cv.VideoCapture(0)
face = cv.imread('Face.jpg')
black = cv.imread('Black.jpg')
blue = cv.imread('Blue.jpg')
brown = cv.imread('Brown.jpg')
green = cv.imread('Green.jpg')
red = cv.imread('Red.jpg')
white = cv.imread('White.jpg')
yellow = cv.imread('Yellow.jpg')



while True:

    _, frame = cap.read()

  #frame shape=(480,640)

    face = frame[0:461, 0:641]

    for z in range(0,23):
        for w in range(0, 32):

            avg0 = 0
            avg1 = 0
            avg2 = 0

            for x in range(20 * z, 20 * (z + 1)):
                for y in range(20 * w, 20 * (w + 1)):
                    avg0 += face.item(x, y, 0)
                    avg1 += face.item(x, y, 1)
                    avg2 += face.item(x, y, 2)

            avg0 = avg0 / 400
            avg1 = avg1 / 400
            avg2 = avg2 / 400

            for x in range(20 * z, 20 * (z + 1)):
                for y in range(20 * w, 20 * (w + 1)):
                    face.itemset((x, y,0),avg0)
                    face.itemset((x, y, 1), avg1)
                    face.itemset((x, y, 2), avg2)

    pixel= cv.resize(frame, (48,64))

    pixel= cv.resize( frame, (480,640))

    cv.imshow('face', face)
    cv.imshow('face', frame)






    key = cv.waitKey(1)
    if key == 27:
        break
