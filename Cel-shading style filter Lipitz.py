import cv2 as cv
import numpy as np

def img_resize(w,h,img):
    width = int(w)
    height = int(h)
    dim = (height,width)
    return cv.resize(img,(width,height))

def edge(img):
    img = cv.Canny(img,55,100)
    return img

'''def basic_color_avg(img,num,cap):
    for i in range(0, int(cap.get(cv.CAP_PROP_FRAME_WIDTH) - num), num):
        for j in range(0, int(cap.get(cv.CAP_PROP_FRAME_HEIGHT) - num), num):
            for k in range(num):
               color1 = cv.add(img[j,i], img[j,(i+k)])
               color2 = cv.add(img[j,i], img[j,(i-k)])
               color3 = cv.add(img[j,i], img[(j+k),(i+k)])
               color4 = cv.add(img[j,i],img[(j-k),(i+k)])
               color5 = cv.add(img[j,i], img[(j+k),(i-k)])
               color6 = cv.add(img[j,i], img[(j-k),(i-k)])
               color7 = cv.add(img[j,i], img[(j+k),i])
               color8 = cv.add(img[j,i], img[(j-k),i])
            
            color = (color1 + color2 + color3 + color4 + color5 + color6 + color7 + color8)/8


            print(color)
            print(img[j,i])
            img[j,i] = color
            img[j,(i+k)] = color
            img[j,(i-k)] = color
            img[(j+k),(i+k)] = color
            img[(j-k),(i+k)] = color
            img[(j+k),(i-k)] = color
            img[(j-k),(i-k)] = color
            img[(j+k),i] = color
            img[(j-k),i] = color
    return img'''





def main():
    eye = cv.imread('Eye3.jpg')
    cap = cv.VideoCapture(0)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
    imgs = []
    frame1 = []
    while True:
        ret, frame = cap.read()
        
        if np.array_equal(frame,frame1):
            print('yay')
        else:
            print('hell')

        for i in range(4):
            imgs.append(frame)
        i=0

        '''imgs[0]=cv.add(imgs[0],np.array([-200.0]))
        imgs[1]=cv.add(imgs[1],np.array([-100.0]))
        imgs[2]=cv.add(imgs[2],np.array([100.0]))
        imgs[3]=cv.add(imgs[3],np.array([200.0]))'''

        img = imgs[1]
        gray = cv.cvtColor(imgs[1], cv.COLOR_BGR2GRAY)
        
        eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
        eyes = eye_cascade.detectMultiScale(gray, 1.3 ,5)
       
        
            
        
        #merge_mertens = cv.createMergeMertens()
        #res_mertens = merge_mertens.process(imgs)
        #res_mertens_8bit = np.clip(res_mertens*255, 0, 255).astype('uint8')

        mask = np.zeros(imgs[1].shape, np.uint8)

        imghsv = cv.cvtColor(imgs[1], cv.COLOR_BGR2HSV).astype("float32")
        

        gray = cv.cvtColor(imgs[1], cv.COLOR_BGR2GRAY)
        edges = cv.Canny(gray,25,150)
        
        (h, s, v) = cv.split(imghsv)
        s = s*1.7
        s = np.clip(s,0,255)
        imghsv = cv.merge([h,s,v])

        imgrgb = cv.cvtColor(imghsv.astype("uint8"), cv.COLOR_HSV2BGR)
        blurred_img =cv.bilateralFilter(imgrgb,20,57,57)

        #thresh = cv.threshold(gray, 60, 255, cv.THRESH_BINARY)[2]
        contours, hierarchy = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        
        
        cv.drawContours(blurred_img, contours, -1, (0,0,0),4)
        #output = np.where(mask==np.array([0, 0, 0]), blurred_img, imgs[1])
        blurred_img_eye = blurred_img.copy()
        
        for (x,y,w,h) in eyes:
            
            temp_eye = img_resize(w,h,eye)

            blurred_img_eye[y:(y+h),x:(x+w)]= temp_eye
            
        lower_white = (245,245,245)
        upper_white = (255,255,255)
        white_mask = cv.inRange(blurred_img_eye, lower_white, upper_white)
        not_white_mask = cv.bitwise_not(white_mask)
        blurred_other_img = cv.bitwise_and(blurred_img_eye, blurred_img_eye, mask=not_white_mask)
        blurred_img_eye = cv.bitwise_and(blurred_img, blurred_img, mask=white_mask)
        final = cv.bitwise_or(blurred_other_img,blurred_img_eye)

       
        cv.imshow('frame', final)
        frame1 = imgs[1]
        imgs = []
        k = cv.waitKey(5) & 0xFF
        if k == 27:
            break


    
main()