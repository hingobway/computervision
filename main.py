import cv2

# TODO: finish annotating

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('facecascade.xml')
fgbg = cv2.createBackgroundSubtractorKNN(detectShadows=False, dist2Threshold=139, history=999999999)


def overlay_transparent(background_img, img_to_overlay_t, x, y, overlay_size=None):
    bg_img = background_img.copy()

    if overlay_size is not None:
        img_to_overlay_t = cv2.resize(img_to_overlay_t.copy(), overlay_size)

    b, g, r, a = cv2.split(img_to_overlay_t)
    overlay_color = cv2.merge((b, g, r))

    mask = cv2.medianBlur(a, 5)

    h, w, _ = overlay_color.shape
    roi = bg_img[y:y + h, x:x + w]

    img1_bg = cv2.bitwise_and(roi.copy(), roi.copy(), mask=cv2.bitwise_not(mask))

    img2_fg = cv2.bitwise_and(overlay_color, overlay_color, mask=mask)

    bg_img[y:y + h, x:x + w] = cv2.add(img1_bg, img2_fg)

    return bg_img


while 1:
    forest = cv2.imread("images/forest.jpg", cv2.IMREAD_COLOR)

    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    fgmask = cv2.medianBlur(fgmask, 15)

    mask1 = cv2.bitwise_and(frame, frame, mask=fgmask)
    fmasked = cv2.bitwise_not(fgmask)
    mask2 = cv2.bitwise_and(forest, forest, mask=fmasked)

    final = cv2.add(mask1, mask2) # Merge foreground (anothing moving) with forest

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