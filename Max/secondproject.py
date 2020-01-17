import cv2

face_cascade = cv2.CascadeClassifier('max_facecascade.xml')
cap = cv2.VideoCapture(0)
length, width = cap.get(3), cap.get(4)

while 1:
    forest = cv2.resize(cv2.imread("max_images/forest-ground-oliver-kluwe.jpg", cv2.IMREAD_COLOR), (int(length), int(width)))  # Resize background with camera's dimensions (prevent size crash)
    photo = cv2.imread("max_images/bear1.png", -1)  # Open bear image and store it in variable "photo"

    _, frame = cap.read()  # Read current frame from video capture, store it in variable "frame"

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Make video capture frame grayscale
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)  # Detect faces in the grayscale frame

    for (x, y, w, h) in faces:  # Loop through all detected faces
        if y < 150 and w < 280:  # If the y-coordinate is less than 150 (meaning it's either within or not within a y-threshold) and the width of the face is less than 280, run the code in the indents
            # This next section of code does the following:
            # After the program has determined that the detected face is over the separation line (between ground and non-ground),
            # the program puts the bear over the separation line and makes the size of the bear entirely dependent on face position.

            height = 293.333333333 - float(y)
            if int(width) < int(y):
                height = width
            if height <= 0:
                height = 0

            bearWidth = (0.512)*(float(height))  # This ratio is the ratio of the image's width to length
        else:
            # If the detected face is not found to be over the separation line, proceed normally

            bearWidth = w  # The width of the bear should = the width of the face
            height = (1.818)*(float(bearWidth))  # This ratio is the ratio of the image's length to width

        # This next section of code determines if the face is near the bottom of the screen.
        # This is an issue because the bear image can't overlay in null space, so we have to crop it using numpy slicing.
        d = float(width) - float(y)
        if height > d:
            photo = photo[0:int(d)]  # This is where numpy slicing happens (crops image's y)
            try:
                photo = cv2.resize(photo.copy(), (int(bearWidth), int(d)))  #  Resize the bruin head to the size of tracked face and store the resized head to variable "img_to_overlay_t"

                bg_img = forest.copy()  # Mirror the background frame and store it in variable "bg_img"

                b, g, r, a = cv2.split(photo)  # Split the (now resized) bruin head into its color components
                overlay_color = cv2.merge((b, g, r))  # Merge all color components except alpha (a) and store it into variable "overlay_color"

                mask = cv2.medianBlur(a, 5)  # Add a blur on the alpha (a) color component by an aperture linear size of 5

                h, w, _ = overlay_color.shape  # Get dimensions from colored part of bruin head

                roi = bg_img[y:y + h, x:x + int(bearWidth)]  # Determine a region of interest (ROI) using the background image and colored part of bruin head dimensions

                img1_bg = cv2.bitwise_and(roi.copy(), roi.copy(), mask=cv2.bitwise_not(mask))  # Use a bitwise_and mask to mask over the region of interest with an inverse of the alpha (create transparency)
                img2_fg = cv2.bitwise_and(overlay_color, overlay_color, mask=mask)  # Do the opposite as above, remove the color part of bruin head

                bg_img[y:y + h, x:x + w] = cv2.add(img1_bg, img2_fg)

                forest = bg_img
            except:
                continue

        # If everything is normal (bear is normally placed in the screen), proceed normally
        try:
            photo = cv2.resize(photo.copy(), (int(bearWidth), int(height)))  #  Resize the bruin head to the size of tracked face and store the resized head to variable "img_to_overlay_t"

            bg_img = forest.copy()  # Mirror the background frame and store it in variable "bg_img"

            b, g, r, a = cv2.split(photo)  # Split the (now resized) bruin head into its color components
            overlay_color = cv2.merge((b, g, r))  # Merge all color components except alpha (a) and store it into variable "overlay_color"

            mask = cv2.medianBlur(a, 5)  # Add a blur on the alpha (a) color component by an aperture linear size of 5

            h, w, _ = overlay_color.shape  # Get dimensions from colored part of bruin head

            roi = bg_img[y:y + h, x:x + w]  # Determine a region of interest (ROI) using the background image and colored part of bruin head dimensions

            img1_bg = cv2.bitwise_and(roi.copy(), roi.copy(), mask=cv2.bitwise_not(mask))  # Use a bitwise_and mask to mask over the region of interest with an inverse of the alpha (create transparency)
            img2_fg = cv2.bitwise_and(overlay_color, overlay_color, mask=mask)  # Do the opposite as above, remove the color part of bruin head

            bg_img[y:y + h, x:x + w] = cv2.add(img1_bg, img2_fg)  # Only keep colored part of bruin head, relocate the image @ opposite corners of the detected face region

            forest = bg_img  # Return the bruin head w/ it's position in the frame
        except:
            continue

    cv2.imshow('img', forest)  # Display the final frame

    # This next code actively checks if N or Z is pressed, and if it is, the program closes
    k = cv2.waitKey(30) & 0xff
    if k == ord('n') or k == ord('z'):
        break

cap.release()
cv2.destroyAllWindows()
