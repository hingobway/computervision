from __future__ import print_function
import cv2 as cv
import argparse
import numpy as np
parser = argparse.ArgumentParser(description='This program shows how to use background subtraction methods provided by \
                                              OpenCV. You can process both videos and images.')
parser.add_argument('--input', type=str, help='Path to a video or a sequence of image.', default='vtest.avi')
parser.add_argument('--algo', type=str, help='Background subtraction method (KNN, MOG2).', default='KNN')

args = parser.parse_args()

#http://www.robindavid.fr/opencv-tutorial/chapter5-line-edge-and-contours-detection.html

## [create]
#create Background Subtractor objects
if args.algo == 'MOG2':
    backSub = cv.createBackgroundSubtractorMOG2()
else:
    backSub = cv.createBackgroundSubtractorKNN(detectShadows=False,dist2Threshold=130,history=599)
## [create]

## [capture]
capture = cv.VideoCapture(0)
capture.set(cv.CAP_PROP_EXPOSURE,-8
            )
lower = np.array([0, 40, 40], dtype = "uint8")
upper = np.array([20, 255, 255], dtype = "uint8")
handmess = "Put your hand in the box"

if not capture.isOpened:
    print('Unable to open: ' + args.input)
    exit(0)
## [capture]
kernel = np.ones((3,3),np.uint8)
color = (255, 0, 0)



while True:
    ret, frame = capture.read()

    # converting from BGR to HSV color space
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
 
    # Range for skin tones
    lower_red = np.array([0,0,50])
    upper_red = np.array([20,255,255])
    
    if frame is None:
        break

    fgMask = backSub.apply(frame)

    fgMask = cv.filter2D(fgMask,-1,kernel)

    

    fgMask = cv.GaussianBlur(fgMask, (5,5), 0)
    
   # fgMask = cv.erode(fgMask, kernel, iterations=1)
    fgMask = cv.medianBlur(fgMask, 15)




    cv.rectangle(frame, (10, 2), (200,20), (255,255,255), -1)

    griffin = "griffin's great test"
    cv.putText(frame, griffin, (15, 15),
               cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
   
    #show the current frame and the fg masks
    mask1 = cv.inRange(hsv, lower_red, upper_red)

    mask1 = cv.medianBlur(mask1, 9)

    frame2 = cv.bitwise_and(frame,frame,mask=mask1)

    fgMask = cv.bitwise_and(frame2,frame2,mask=fgMask)
     
    start_point = (50, 50) 
      
    end_point = (220, 220) 
      
    # Blue color in BGR 
      
    # Line thickness of 2 px 
    thickness = 2
      # Crop image
 
    # Display cropped image
    fgMask = cv.rectangle(fgMask, start_point, end_point, color, thickness) 
 

    roi = fgMask[51:219,51:219]
    





    gray = cv.cvtColor(roi,cv.COLOR_BGR2GRAY)
    gray = cv.GaussianBlur(gray,(5,5),0)
    ret,thresh1 = cv.threshold(gray,100,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
    contours,hierarchy = cv.findContours(thresh1, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    if len(contours) != 0:
        # draw in blue the contours that were founded
        cv.drawContours(roi, contours, -1, 255, 3)

        # find the biggest countour (c) by the area
        c = max(contours, key = cv.contourArea)
        x,y,w,h = cv.boundingRect(c)

        # draw the biggest contour (c) in green
        cv.rectangle(roi,(x,y),(x+w,y+h),(0,255,0),2)
        color = (255-(len(contours)*25), 10, len(contours)*25) 
      
        
       # roi = cv.bitwise_and(roi,roi,mask=drawing)
        cv.rectangle(fgMask, (10, 2), (300,20), (255,255,255), -1)
        cv.putText(fgMask, handmess, (15, 15),
                    cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))

    res = cv.bitwise_and(frame, frame, mask=mask1)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blurValue = 3
    blur = cv.GaussianBlur(gray, (blurValue, blurValue), 0)

    ret, thresh = cv.threshold(blur, 1, 255, cv.THRESH_BINARY)

    contours, hierarchy = cv.findContours(thresh1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    #hull = cv.convexHull(res)
    #defects = cv.convexityDefects(res, hull)




    #cv.imshow('roi', roi)
    cv.imshow('input', frame)
    #cv.imshow('Frame2', frame2)
   # cv.imshow('colormask',mask1)
    cv.imshow('output', fgMask)
    #cv.imshow('draw', drawing)
    ## [show]
    

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        cv.destroyAllWindows()
        capture.release()  
        break
    
    
    
