import cv2

cap = cv2.VideoCapture(0)  # Get video capture by device ID & store it in variable "cap"
face_cascade = cv2.CascadeClassifier('facecascade.xml')  # Load the haar cascade & store it in variable "face_cascade"
fgbg = cv2.createBackgroundSubtractorKNN(detectShadows=False, dist2Threshold=139, history=999999999)  # Store background subtraction algorithm KNN into variable "fgbg"


def overlay_transparent(background_img, img_to_overlay_t, x, y, overlay_size):
    # Function to overlay a transparent image on another, source 1

    img_to_overlay_t = cv2.resize(img_to_overlay_t.copy(), overlay_size)  #  Resize the bruin head to the size of tracked face and store the resized head to variable "img_to_overlay_t"

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


while 1:  # This code in this loop will be looped forever
    forest = cv2.imread("images/forest.jpg", cv2.IMREAD_COLOR)  # Read "forest.jpg" in folder "images" and store it in variable "forest"

    _, frame = cap.read()  # Read the current frame and store it in variable "frame"

    fgmask = fgbg.apply(frame)  # Apply the background subtraction algorithm to the current frame, store in variable "fgmask" (stands for foreground mask)

    fgmask = cv2.medianBlur(fgmask, 15)  # Apply a blur to the foreground mask with an intensity of 15

    mask1 = cv2.bitwise_and(frame, frame, mask=fgmask)  # Remove all moving things from the frame, store in variable "mask1"
    fmasked = cv2.bitwise_not(fgmask)  # Invert the foreground mask, will effectively create a background mask. store in variable "fmasked"
    mask2 = cv2.bitwise_and(forest, forest, mask=fmasked)  # Use the inverted foreground mask to replace background with forest photo (anything that is static in the frame is cut out, and everything left is the forest photo)

    final = cv2.add(mask1, mask2)  # Merge foreground (anything moving) with forest

    bruin_head = cv2.imread("images/test.png", -1)

    gray = cv2.cvtColor(final, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        final = overlay_transparent(final, bruin_head, x, y, (w, h))

    cv2.imshow('Feed', final)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
