import pdfplumber
from pdf2image import convert_from_bytes
import pytesseract
from PIL import Image
import io

def extract_text_from_file(file_bytes, file_extension):
    extracted_text = ""
    try:
        if file_extension in ["png", "jpg", "jpeg"]:
            image = Image.open(io.BytesIO(file_bytes))
            extracted_text = pytesseract.image_to_string(image)
        elif file_extension == "pdf":
            with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        extracted_text += text + "\n"
            
            # Fallback to OCR if PDF is scanned / has no text layer
            if len(extracted_text.strip()) < 50:
                images = convert_from_bytes(file_bytes)
                for img in images:
                    ocr_text = pytesseract.image_to_string(img)
                    extracted_text += ocr_text + "\n"
    except Exception as e:
        print(f"Error during text extraction: {e}")
        
    return extracted_text