import pytesseract
from pdf2image import convert_from_path


POPPLER_PATH = r"C:\Users\LENOVO\Downloads\Release-26.07.0-0\poppler-26.07.0\Library\bin"

TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH


def extract_text_from_pdf(pdf_path):
    pages = convert_from_path(
        pdf_path,
        poppler_path=POPPLER_PATH
    )

    extracted_text = ""

    for page_number, page in enumerate(pages, start=1):
        text = pytesseract.image_to_string(page)

        extracted_text += f"\n--- Page {page_number} ---\n"
        extracted_text += text

    return extracted_text