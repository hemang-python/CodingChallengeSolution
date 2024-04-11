import streamlit as st
import requests


def main():
    """Streamlit frontend to upload PDF files and display extracted text"""
    st.title("PDF Document Text Extractor")

    uploaded_file = st.file_uploader("Upload PDF File", type=["pdf"])

    if uploaded_file:
        if st.button("Convert"):
            files = {"file": uploaded_file}
            try:
                response = requests.post("http://localhost:8000/upload/", files=files)
                response.raise_for_status()
                texts = response.json()
                st.write("Extracted Texts:")
                for text in texts:
                    st.write(text)
            except Exception as e:
                st.error(f"Error: {e}")


if __name__ == "__main__":
    main()
