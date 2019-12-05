import cv2

face_cascade = cv2.CascadeClassifier('facecascade.xml')
cap = cv2.VideoCapture(0)
length, width = cap.get(3), cap.get(4)


def overlay_transparent(background_img, img_to_overlay_t, x, y, w,h):
    # Function to overlay a transparent image on another, source 1

    img_to_overlay_t = cv2.resize(img_to_overlay_t.copy(), (w, h))  #  Resize the bruin head to the size of tracked face and store the resized head to variable "img_to_overlay_t"

    bg_img = background_img.copy()  # Mirror the background frame and store it in variable "bg_img"

    b, g, r, a = cv2.split(img_to_overlay_t)  # Split the (now resized) bruin head into its color components
    overlay_color = cv2.merge((b, g, r))  # Merge all color components except alpha (a) and store it into variable "overlay_color"

    mask = cv2.medianBlur(a, 5)  # Add a blur on the alpha (a) color component by an aperture linear size of 5

    h, w, _ = overlay_color.shape  # Get dimensions from colored part of bruin head
    roi = bg_img[y:y + h, x:x + w]  # Determine a region of interest (ROI) using the background image and colored part of bruin head dimensions

    img1_bg = cv2.bitwise_and(roi.copy(), roi.copy(), mask=cv2.bitwise_not(mask))  # Use a bitwise_and mask to mask over the region of interest with an inverse of the alpha (create transparency)

    img2_fg = cv2.bitwise_and(overlay_color, overlay_color, mask=mask)  # Do the opposite as above, remove the color part of bruin head

    bg_img[y:y + h, x:x + w] = cv2.add(img1_bg, img2_fg)  # Only keep colored part of bruin head, relocate the image @ opposite corners of the detected face region

    return bg_img  # Return the bruin head w/ it's position in the frame


while 1:
    forest = cv2.resize(cv2.imread("images/background.jpg", cv2.IMREAD_COLOR), (int(length), int(width)))
    photo = cv2.imread("images/bear1.png", -1)

    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        # cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        forest = overlay_transparent(forest, photo, x, y, w, h)

    cv2.imshow('img', forest)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
