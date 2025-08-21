import cv2, os, re
from detector import detect_text_regions, run_ocr_on_regions
from masking import mask_region
from utils import save_report
from ner_huggingface import detect_names

INPUT_DIR = "../data"
OUTPUT_DIR = "../outputs"

SSN_REGEX = r"\b\d{3}-\d{2}-\d{4}\b"
DOB_REGEX = r"\b\d{2}/\d{2}/\d{4}\b"

def process_image(filename):
    img = cv2.imread(os.path.join(INPUT_DIR, filename))
    regions = detect_text_regions(img)
    texts = run_ocr_on_regions(img, regions)

    masked_items = []

    for text, (x,y,w,h) in texts:
        if re.match(SSN_REGEX, text):
            img = mask_region(img, x, y, w, h, method="black")
            masked_items.append({"type":"SSN", "text":text})

        elif re.match(DOB_REGEX, text):
            img = mask_region(img, x, y, w, h, method="blur")
            masked_items.append({"type":"DOB", "text":text})

        else:
            names = detect_names(text)
            if names:
                img = mask_region(img, x, y, w, h, method="black")
                masked_items.append({"type":"Name", "text":text})

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(OUTPUT_DIR, f"masked_{filename}")
    cv2.imwrite(out_path, img)
    save_report(filename, masked_items)

    print(f"[+] Processed {filename} → {out_path}")

if __name__ == "__main__":
    for file in os.listdir(INPUT_DIR):
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            process_image(file)
