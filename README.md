# Personal Information Masking Tool 🔒

## 📌 Overview
This project automatically detects and masks sensitive information (SSNs, Names, DOB, etc.) from scanned ID documents.

## ⚙️ Tech Stack
- **OCR**: Tesseract OCR (option: Google Vision API)
- **NER**: spaCy, HuggingFace Transformers
- **Visual Layout**: YOLOv5 (future enhancement)
- **Image Processing**: OpenCV, Pillow
- **Backend (future)**: Flask

## 🚀 How It Works
1. **Detect text regions** (YOLO planned, Tesseract fallback used now)
2. **Extract text** with OCR
3. **Identify sensitive info** using Regex + NER
4. **Mask regions** (black, blur, pixelation)
5. **Save outputs**:
   - Masked image (`/outputs`)
   - JSON report (`/reports`)

## 📂 Project Structure
```
personal-info-masking/
 ├── data/       # input images
 ├── outputs/    # masked results
 ├── reports/    # json logs
 ├── src/        # source code
 ├── requirements.txt
 └── README.md
```

## ▶️ Run
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
cd src
python main.py
```

## 📊 Example (Before & After)
| Input | Masked Output |
|-------|---------------|
| ![input](data/sample.png) | ![output](outputs/masked_sample.png) |

## 🔮 Future Work
- Add phone number + address masking
- Support cloud deployment
- Interactive web interface
