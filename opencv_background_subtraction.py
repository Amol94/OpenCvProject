import numpy as np
import cv2

cap = cv2.VideoCapture('vtest.avi')
# fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
# fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)
# fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
fgbg = cv2.createBackgroundSubtractorKNN(detectShadows=False)
while True:
    ret, frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame)
    # fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    cv2.imshow('Frame', frame)
    cv2.imshow('FG MASK Frame', fgmask)

    keybord = cv2.waitKey(30)

    if keybord == 'q' or keybord == 27:
        break

cap.release()
cv2.destroyAllWindows()