import cv2 as cv
import random

# load the required trained XML classifiers 
# https://github.com/Itseez/opencv/blob/master/ 
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml') 

# capture frames from a camera 
cap = cv.VideoCapture(0) 

wonLevel1 = False #at the beginning of the game, the player
wonLevel2 = True #hasn't won any of the levels
wonLevel3 = False

bluex = random.randrange(0, 200) #randomize goal locations for Level 3
bluey = random.randrange(200,400) #every time a new game is begun
bluew = 0
blueh = 0
greenx = random.randrange(500,700)
greeny = random.randrange(0,700)
greenw = 0
greenh = 0
redx = random.randrange(0,700)
redy = random.randrange(0,500)
redw = 0
redh = 0

print("Blue ", bluex, bluey)
print("Green ", greenx, greeny)
print("Blue ", redx, redy)

inBox1 = False
inBox2 = False
inBox3 = False


while 1: #loop runs if capturing has been initialized
    ret, img = cap.read()
    k = cv.waitKey(30) & 0xff
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #convert frame to grayscale
    numFaces = 0 #default faces in the frame is zero

    if inBox1 == True:
        cv.rectangle(img,(bluex,bluey),(bluex+bluew,bluey+blueh),(255,255,0),2) #note: if you use x,y and not bluex,bluey , very weird effect!
    if inBox2 == True:
        cv.rectangle(img,(greenx,greeny),(greenx+greenw,greeny+greenh),(0,255,0),2)
    if inBox3 == True:
        cv.rectangle(img,(redx,redy),(redx+redw,redy+redh),(0,0,255),2)
    

    faces = face_cascade.detectMultiScale(gray, 1.3, 5) #use cascade to detect faces
    for (x,y,w,h) in faces: #for each face found
        numFaces += 1 #increment numFaces
        if wonLevel2 == True: #if we're on Level 3 already
            if inBox1 == False:
                if x>bluex and x<(bluex+100) and bluey and bluey+100: #if face in first set of random coords
                    cv.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) #draw a blueish-greenish box around face
                    inBox1 = True
                    bluex = x
                    bluey = y
                    bluew = w
                    blueh = h
                else: inBox1 = False 
            if inBox2 == False:  
                if x>greenx and x<(greenx+100) and y>greeny and y<(greeny+100): #if face in second set of random coords
                    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) #draw green box
                    inBox2 = True
                    greenx = x
                    greeny = y
                    greenw = w
                    greenh = h
                else: inBox2 = False
            if inBox3 == False:
                if x>redx and x<(redx+100) and y>redy and y<(redy+100): #if face in third set of random coords
                    cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) #draw red box
                    inBox3 = True
                    redx = x
                    redy = y
                    redw = w
                    redh = h
                else: inBox3 = False
    

    if inBox1 == True and inBox2 == True and inBox3 == True: #shows different text if you've won
        cv.putText(img, "Congratulations! You won the game!",(300,50), cv.FONT_HERSHEY_PLAIN, 2.5, (255,255,0), 2, cv.LINE_AA)
    else:
        cv.putText(img, "Find all three different color boxes!",(300,50), cv.FONT_HERSHEY_PLAIN, 2.5, (255,0,0), 2, cv.LINE_AA)

    cv.imshow('img',img)

    if k == 27:
        break

# Close the window 
cap.release() 

# De-allocate any associated memory usage 
cv.destroyAllWindows() 