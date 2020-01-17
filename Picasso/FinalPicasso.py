import cv2 as cv
import numpy as np
import tkinter as tk


def nothing(x):
    pass

def artaverage():
    while True:


        vinny = cv.resize(vincenti, (int(cap.get(3)), int(cap.get(4))))

        _, frame = cap.read()
        # for i in range (1,3):
        # blur = cv.filter2D(frame,-1,kernel,None, (-i,-i))

        factor = cv.getTrackbarPos("Pixelsize", "Tracks")

        if factor <= 3:
            pixel = frame

        if not(factor <= 3):

            vinny1 = cv.resize(vinny, (int(cap.get(3)) // factor, int(cap.get(4)) // factor), interpolation=cv.INTER_NEAREST)

            pixel = cv.resize(frame, (int(cap.get(3)) // factor, int(cap.get(4)) // factor), interpolation=cv.INTER_NEAREST)

            for x in range(0, int(cap.get(4)) // factor):
                for y in range(0, int(cap.get(3)) // factor):

                    avg0 = pixel.item(x, y, 1)

                    matr = avg0 * np.ones((int(cap.get(4)) // factor, int(cap.get(3)) // factor))

                    diff = np.absolute(np.subtract(vinny1[:, :, 1], matr))

                    result = np.where(diff == np.amin(diff))

                    LOC = list(zip(result[0], result[1]))

                    r0 = result[0]
                    r1 = result[1]

                    if (r0[0] == int(cap.get(4)) // factor - 1 or r1[0] == int(cap.get(3)) // factor - 1):


                        pass


                    else:
                        fullboi = vinny[(r0[0]) * factor: (r0[0] + 1) * factor, (r1[0]) * factor:(r1[0] + 1) * factor]

                        frame[x * factor: (x + 1) * factor, y * factor: (y + 1) * factor] = fullboi

            pixel = cv.resize(pixel, (int(cap.get(3)), int(cap.get(4))), interpolation=cv.INTER_NEAREST)

        cv.imshow('frame', frame)

        cv.imshow('painting', vinny)


        key = cv.waitKey(1)
        if key == 27:
            break

def artaverage1():

    global vincenti

    vincenti = vincenzo

    artaverage()

def artaverage2():
    global vincenti

    vincenti = munch

    artaverage()



cap = cv.VideoCapture(0)


munch = cv.imread('scream.jpg')
vincenzo = cv.imread('StarryNight.jpg')
wave = cv.imread('GreatWave.jpg')
lisa = cv.imread('Mona.jpg')




vincenti = vincenzo





while True:


    cv.namedWindow("Tracks")
    cv.createTrackbar("Pixelsize", "Tracks", 40, 100, nothing)

    a1 = int(cap.get(4)) - cv.getTrackbarPos("Pixelsize", "Tracks")

    a2 = int(cap.get(3)) - cv.getTrackbarPos("Pixelsize", "Tracks")



    key2 = cv.waitKey(1)

    if key2 == 27:

       break


    if key2 == ord('w'):
        artaverage2()

    if key2 == ord('q'):
        artaverage1()


cv.destroyAllWindows()