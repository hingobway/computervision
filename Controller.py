
import cv2 as cv
import numpy as np
import subprocess

frame = cv.imread('Mona.jpg')

while True:


    cv.imshow('frame', frame)


    key = cv.waitKey(1)


    if key == ord('q'):

        subprocess.call(['python', 'FinalPicasso.py'])




    if key == ord('a'):

        subprocess.call(['python', 'HandTrack.py'])


    if key == ord('z'):
        exec('FinalPicasso')

    if key == ord('w'):
        exec('FinalPicasso')

    if key == ord('s'):
        exec('FinalPicasso')

    if key == ord('x'):
        exec('FinalPicasso')

    if key == ord('e'):
        exec('FinalPicasso')

    if key == ord('d'):
        exec('FinalPicasso')



