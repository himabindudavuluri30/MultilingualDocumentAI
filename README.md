# 📄 Multilingual Document AI

A document intelligence system that processes PDF documents using OCR, language detection, translation, and text summarization.

## 🚀 Features

* 📄 Upload PDF documents
* 🔍 Extract text from scanned PDFs using OCR
* 🌍 Detect the document language
* 🔄 Translate extracted text into English
* 📝 Generate concise summaries
* 🖥️ Interactive Streamlit web interface

## 🏗️ Architecture

```text
PDF Document
     ↓
    OCR
     ↓
Language Detection
     ↓
 Translation
     ↓
Summarization
     ↓
Streamlit Interface
```

## 🛠️ Technologies Used

* Python
* Streamlit
* Tesseract OCR
* Poppler
* PyTorch
* Hugging Face Transformers
* LangDetect
* pdf2image

## 📁 Project Structure

```text
MultilingualDocumentAI/
│
├── utils/
│   ├── __init__.py
│   ├── ocr.py
│   ├── language.py
│   ├── translator.py
│   └── summarizer.py
│
├── uploads/
├── app.py
├── test_ocr.py
├── test_language.py
├── test_translation.py
├── test_summarizer.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/himabindudavuluri30/MultilingualDocumentAI.git
```

Navigate into the project:

```bash
cd MultilingualDocumentAI
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🔧 External Dependencies

This project requires:

### Tesseract OCR

Install Tesseract OCR and update the path in `utils/ocr.py` if necessary.

### Poppler

Install Poppler for Windows and update the Poppler path in `utils/ocr.py` if necessary.

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal.

## 🧪 Testing

Individual components can be tested using:

```bash
python test_ocr.py
python test_language.py
python test_translation.py
python test_summarizer.py
```

## 🔮 Future Improvements

* Support multiple source languages
* Improve OCR accuracy
* Add multilingual translation using a multilingual translation model
* Add document question answering
* Add RAG-based document search
* Support multiple document formats
* Improve UI and document processing performance


GitHub: https://github.com/himabindudavavuri30
