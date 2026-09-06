import streamlit as st

from utils.ocr import extract_text_from_pdf
from utils.language import detect_language
from utils.translator import translate_text
from utils.summarizer import summarize_text


st.set_page_config(
    page_title="Multilingual Document AI",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Multilingual Document AI")
st.write(
    "Upload a PDF to extract text, detect its language, "
    "translate it, and generate a summary."
)

uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    pdf_path = "uploads/uploaded_document.pdf"

    with open(pdf_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    st.success("PDF uploaded successfully!")

    if st.button("🚀 Process Document"):

        with st.spinner("Extracting text with OCR..."):
            text = extract_text_from_pdf(pdf_path)

        st.subheader("📝 Extracted Text")
        st.text_area(
            "OCR Output",
            text,
            height=300
        )

        with st.spinner("Detecting language..."):
            language = detect_language(text)

        st.info(f"🌍 Detected Language: {language}")

        if language == "en":
            translated_text = text
        else:
            with st.spinner("Translating to English..."):
                translated_text = translate_text(text)

        st.subheader("🔄 English Translation")
        st.text_area(
            "Translated Text",
            translated_text,
            height=300
        )

        with st.spinner("Generating summary..."):
            summary = summarize_text(translated_text)

        st.subheader("📌 Summary")
        st.write(summary)