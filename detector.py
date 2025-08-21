import pytesseract
import re
import cv2

def detect_text_regions(img):
    h, w = img.shape[:2]
    return [(0, 0, w, h)]

def run_ocr_on_regions(img, regions):
    results = []
    for (x, y, w, h) in regions:
        roi = img[y:y+h, x:x+w]
        text = pytesseract.image_to_string(roi)
        results.append((text.strip(), (x, y, w, h)))
    return results
