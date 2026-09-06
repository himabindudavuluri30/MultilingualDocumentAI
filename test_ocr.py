from utils.ocr import extract_text_from_pdf

pdf_path = "uploads/The Silent Patient - Alex Michaelides - Alex Michaelides.pdf"

text = extract_text_from_pdf(pdf_path)

print(text)