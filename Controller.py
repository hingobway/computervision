
import cv2 as cv
import numpy as np
import subprocess

frame = cv.imread('Picasso/Mona.jpg')

while True:


    cv.imshow('frame', frame)


    key = cv.waitKey(1)


    if key == ord('q'):

        subprocess.call(['python3', 'Picasso/FinalPicasso.py'])


    if key == ord('a'):

        subprocess.call(['python3', 'GriffinFinal.py'])


    if key == ord('z'):
        subprocess.call(['python3', 'Cel-shading style filter Lipitz.py'])

    if key == ord('w'):
        subprocess.call(['python3', 'blur4.py'])

    if key == ord('s'):
        subprocess.call(['python3', 'Max/firstproject.py'])

    if key == ord('x'):
        subprocess.call(['python3', 'Max/secondproject.py'])


    if key == ord('e'):
        subprocess.call(['python3', 'pspaint/main.py'])

    if key == ord('d'):
        subprocess.call(['python3', 'PresentationProgram/Puppet Presentation.py'])




