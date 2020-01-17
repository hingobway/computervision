import cv2 as cv
import numpy as np
from playsound import playsound
import time
#1280x720
#mp3 = 50, 51, 54, 79, scream
direction = False
buttonPress = False
chapter = 0
picture = cv.imread("Pictures/title.png", cv.IMREAD_COLOR)
cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
def chapterCheck(x):
    global chapter
    global picture
    global buttonPress
    sayOnce = True
    chapter = cv.getTrackbarPos("Chapter", "trackbar")
    if chapter == 0:
        pass
    elif chapter == 17:
        picName = "Pictures/" + str(chapter) + ".png"
        soundName = "Audio/" + str(chapter) + ".wav"
        picture = cv.imread(picName, cv.IMREAD_COLOR)
        playsound.playsound(soundName, False)
    elif chapter == 19 or chapter == 20 or chapter == 21:
        picName = "Pictures/" + str(chapter) + ".png"
        picture = cv.imread(picName, cv.IMREAD_COLOR)
        playsound.playsound("Audio/Whoosh.wav", False)
    elif chapter == 25 or chapter == 27 or chapter == 29:
        picName = "Pictures/" + str(chapter) + ".png"
        picture = cv.imread(picName, cv.IMREAD_COLOR)
    elif chapter == 26 or chapter == 28:
        picName = "Pictures/" + str(chapter) + ".png"
        picture = cv.imread(picName, cv.IMREAD_COLOR)
        playsound.playsound("Audio/ShootingSound.wav", False)
    elif chapter == 30:
        picName = "Pictures/" + str(chapter) + ".png"
        picture = cv.imread(picName, cv.IMREAD_COLOR)
        playsound.playsound("Audio/ExplosionSound.wav", False)
    elif chapter == 50:
        picName = "Pictures/" + str(chapter) + ".png"
        picture = cv.imread(picName, cv.IMREAD_COLOR)
        playsound.playsound("Audio/50.mp3", False)
    elif chapter == 51:
        picName = "Pictures/" + str(chapter) + ".png"
        picture = cv.imread(picName, cv.IMREAD_COLOR)
        playsound.playsound("Audio/51.mp3", False)
    elif chapter == 54:
        picName = "Pictures/" + str(chapter) + ".png"
        picture = cv.imread(picName, cv.IMREAD_COLOR)
        playsound.playsound("Audio/54.mp3", False)
    elif chapter == 59:
        picName = "Pictures/" + str(chapter) + ".png"
        picture = cv.imread(picName, cv.IMREAD_COLOR)
    elif chapter == 61:
        picName = "Pictures/" + str(chapter) + ".png"
        picture = cv.imread(picName, cv.IMREAD_COLOR)
        playsound.playsound("Audio/Whoosh.wav", False)
        playsound.playsound("Audio/ExplosionSound.wav", False)
    elif chapter == 62:
        picName = "Pictures/" + str(chapter) + ".png"
        picture = cv.imread(picName, cv.IMREAD_COLOR)
        playsound.playsound("Audio/Whoosh.wav", False)
    elif chapter == 63:
        picName = "Pictures/" + str(chapter) + ".png"
        picture = cv.imread(picName, cv.IMREAD_COLOR)
        playsound.playsound("Audio/Whoosh.wav", False)
    elif chapter == 64:
        picName = "Pictures/" + str(chapter) + ".png"
        picture = cv.imread(picName, cv.IMREAD_COLOR)
        playsound.playsound("Audio/Whoosh.wav", False)
    elif chapter == 65:
        picName = "Pictures/" + str(chapter) + ".png"
        picture = cv.imread(picName, cv.IMREAD_COLOR)
        playsound.playsound("Audio/ExplosionSound.wav", False)
    elif chapter == 66:
        picName = "Pictures/" + str(chapter) + ".png"
        picture = cv.imread(picName, cv.IMREAD_COLOR)
    elif chapter == 71:
        picName = "Pictures/" + str(chapter) + ".png"
        picture = cv.imread(picName, cv.IMREAD_COLOR)
    elif chapter == 72:
        picName = "Pictures/" + str(chapter) + ".png"
        picture = cv.imread(picName, cv.IMREAD_COLOR)
    elif chapter == 79:
        picName = "Pictures/" + str(chapter) + ".png"
        picture = cv.imread(picName, cv.IMREAD_COLOR)
        playsound.playsound("Audio/79.mp3", False)
    elif chapter == 80:
        picName = "Pictures/" + str(chapter) + ".png"
        picture = cv.imread(picName, cv.IMREAD_COLOR)
    elif chapter == 81:
        picName = "Pictures/" + str(chapter) + ".png"
        picture = cv.imread(picName, cv.IMREAD_COLOR)
    elif chapter == 82:
        picName = "Pictures/" + str(chapter) + ".png"
        picture = cv.imread(picName, cv.IMREAD_COLOR)
    elif chapter == 83:
        picName = "Pictures/" + str(chapter) + ".png"
        picture = cv.imread(picName, cv.IMREAD_COLOR)
    else:
        picName = "Pictures/" + str(chapter) + ".png"
        soundName = "Audio/" + str(chapter) + ".wav"
        picture = cv.imread(picName, cv.IMREAD_COLOR)
        playsound.playsound(soundName, False)
cv.namedWindow("trackbar")
cv.createTrackbar("Chapter", "trackbar", 0, 83, chapterCheck)
font = cv.FONT_HERSHEY_COMPLEX
skip = False
'''
#SETTING UP COLOR SPACES
gl1 = 0
gl2 = 0
gl3 = 0
gu1 = 0
gu2 = 0
gu3 = 0
def changeValues(x):
    global gl1
    global gl2
    global gl3
    global gu1
    global gu2
    global gu3
    gl1 = cv.getTrackbarPos("gl1", "Color")
    gl2 = cv.getTrackbarPos("gl2", "Color")
    gl3 = cv.getTrackbarPos("gl2", "Color")
    gu1 = cv.getTrackbarPos("gu1", "Color")
    gu2 = cv.getTrackbarPos("gu2", "Color")
    gu3 = cv.getTrackbarPos("gu3", "Color")
cv.namedWindow("Color")
cv.createTrackbar("gl1", "Color", 0, 255, changeValues)
cv.createTrackbar("gl2", "Color", 0, 255, changeValues)
cv.createTrackbar("gl3", "Color", 0, 255, changeValues)
cv.createTrackbar("gu1", "Color", 0, 255, changeValues)
cv.createTrackbar("gu2", "Color", 0, 255, changeValues)
cv.createTrackbar("gu3", "Color", 0, 255, changeValues)
#SETTING UP COLOR SPACES
'''
while(1):
    _, frame = cap.read()
    _, frame2 = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    '''
    lower_orange = np.array([69,37,19])
    upper_orange = np.array([88,239,255])
    '''
    lower_orange = np.array([5,102,195])
    upper_orange = np.array([25,190,255])
    maskOrange = cv.inRange(hsv, lower_orange, upper_orange)
    step1 = cv.bitwise_and(frame2, frame2, mask=maskOrange)
    step2 = cv.bitwise_not(maskOrange)
    step3 = cv.bitwise_and(picture, picture, mask=step2)
    final = cv.add(step1, step3)
    if chapter == 26 and chapter == 28:
        num = chapter + 1
        cv.setTrackbarPos("Chapter", "trackbar", num)
    #circle detection
    if chapter == 17 or chapter == 25 or chapter == 27 or chapter == 29 or chapter == 33 or chapter == 45 or chapter == 50:
        edges = cv.Canny(maskOrange, 200, 200)
        circles = cv.HoughCircles(edges,cv.HOUGH_GRADIENT,1,1000,param1=90,param2=21,minRadius=30,maxRadius=300)
        '''
        cv.rectangle(final, (590, 320), (700, 440), (255,0,0), -1)
        '''
        if circles is not None:
            circles1 = np.round(circles[0, :]).astype("int")
            x, y = circles1[0][0], circles1[0][1]
            for (x, y, r) in circles1:
                if chapter == 17:
                    if x < 310 and x > 200 and y > 210 and y < 260:
                            num = chapter + 1
                            cv.setTrackbarPos("Chapter", "trackbar", num)
                elif chapter == 25:
                    if x < 680 and x > 600 and y > 320 and y < 400:
                            num = chapter + 1
                            cv.setTrackbarPos("Chapter", "trackbar", num)
                            skip = True
                elif chapter == 27:
                    if x < 680 and x > 600 and y > 30 and y < 120:
                            num = chapter + 1
                            cv.setTrackbarPos("Chapter", "trackbar", num)
                            skip = True
                elif chapter == 29:
                    if x < 680 and x > 600 and y > 600 and y < 680:
                            num = chapter + 1
                            cv.setTrackbarPos("Chapter", "trackbar", num)
                elif chapter == 33:
                    if x < 500 and x > 380 and y > 150 and y < 330:
                            num = chapter + 1
                            cv.setTrackbarPos("Chapter", "trackbar", num)
                elif chapter == 45:
                    if x > 1000 and y > 250 and y < 450:
                            num = chapter + 1
                            cv.setTrackbarPos("Chapter", "trackbar", num)
                elif chapter == 50:
                    if x < 710 and x > 580 and y > 300 and y < 440:
                            num = chapter + 1
                            cv.setTrackbarPos("Chapter", "trackbar", num)
            #Showing circle
                            '''
            circles2 = np.uint16(np.around(circles))
            for i in circles2[0,:]:           
                cv.circle(final,(i[0],i[1]),i[2],(255,0,0),-1)
            '''
    cv.imshow("trackbar", final)
    k = cv.waitKey(5) & 0xFF
    print (k)
    if k == 122 and chapter != 17 and chapter != 25 and chapter != 27 and chapter != 29 and chapter != 33 and chapter != 50:
        num = chapter + 1
        cv.setTrackbarPos("Chapter", "trackbar", num)
    elif chapter == 26 or chapter == 28:
        if skip == False:
            time.sleep(1)
            num = chapter + 1
            cv.setTrackbarPos("Chapter", "trackbar", num)
    elif k == 27:
        break
    skip = False
cv.destroyAllWindows()
