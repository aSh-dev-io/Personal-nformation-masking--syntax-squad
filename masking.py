import cv2

def mask_region(img, x, y, w, h, method="black"):
    if method == "black":
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), -1)
    elif method == "blur":
        roi = img[y:y+h, x:x+w]
        blur = cv2.GaussianBlur(roi, (25, 25), 30)
        img[y:y+h, x:x+w] = blur
    elif method == "pixelate":
        roi = img[y:y+h, x:x+w]
        h_, w_ = roi.shape[:2]
        temp = cv2.resize(roi, (10, 10), interpolation=cv2.INTER_LINEAR)
        pixelated = cv2.resize(temp, (w_, h_), interpolation=cv2.INTER_NEAREST)
        img[y:y+h, x:x+w] = pixelated
    return img
