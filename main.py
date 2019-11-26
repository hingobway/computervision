import cv2

cap = cv2.VideoCapture(0)  # Get video capture by device ID & store it in variable "cap"
face_cascade = cv2.CascadeClassifier('facecascade.xml')  # Load the haar cascade & store it in variable "face_cascade"
fgbg = cv2.createBackgroundSubtractorKNN(detectShadows=False, dist2Threshold=139, history=999999999)  # Store background subtraction algorithm KNN into variable "fgbg"
length, width = cap.get(3), cap.get(4)  # Get dimensions of video capture
forest = cv2.resize(cv2.imread("images/forest.jpg", cv2.IMREAD_COLOR), (int(length), int(width)))  # Read "forest.jpg" in folder "images" & resize it to dimensions of video capture, store in variable "forest"


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
    _, frame = cap.read()  # Read the current frame and store it in variable "frame"

    fgmask = fgbg.apply(frame)  # Apply the background subtraction algorithm to the current frame, store in variable "fgmask" (stands for foreground mask)

    fgmask = cv2.medianBlur(fgmask, 15)  # Apply a blur to the foreground mask with an intensity of 15

    mask1 = cv2.bitwise_and(frame, frame, mask=fgmask)  # Remove all moving things from the frame, store in variable "mask1"
    fmasked = cv2.bitwise_not(fgmask)  # Invert the foreground mask, will effectively create a background mask. store in variable "fmasked"
    mask2 = cv2.bitwise_and(forest, forest, mask=fmasked)  # Use the inverted foreground mask to replace background with forest photo (anything that is static in the frame is cut out, and everything left is the forest photo)

    final = cv2.add(mask1, mask2)  # Merge foreground (anything moving) with forest

    bruin_head = cv2.imread("images/test.png", -1)  # Load bruin head image and store it to variable "bruin_head"

    gray = cv2.cvtColor(final, cv2.COLOR_BGR2GRAY)  # Make the foreground + forest frame grayscale
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)  # Use haar cascade algorithm to detect faces in the grayscale frame, store each face to array "faces"

    for (x, y, w, h) in faces:  # Range over all faces and grab position and dimension info
        final = overlay_transparent(final, bruin_head, x, y, (w, h))  # For each respective face, overlay a bruin head using collected info (coordinates, dimensions)

    cv2.imshow('Feed', final)  # Show the final product

    # This next part is standard Python procedure to exit out of a program.
    # First, it checks to see if the ESC (escape) key is clicked.
    # If it isn't, the program continues looping.
    # If it is pressed, the loop "breaks," or more notably, ends and runs the final two lines of code.
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# These two lines create a "safe" exit within OpenCV.
# First, the capture device is released.
# Lastly, all windows are safely closed.
# If the program came to an instant halt, there is a small possibility that the damage would bug your OS (operating system). It's better to be safe.
cap.release()
cv2.destroyAllWindows()
