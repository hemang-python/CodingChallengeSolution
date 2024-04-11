# Document Text Extractor App

## Overview
An application that allows users to upload PDF documents through a Streamlit interface. The backend, developed with FastAPI, processes these uploads by converting the PDFs into plain text. The converted text will then be displayed back to the user within the Streamlit interface.

## Requirements
- **Python 3.8+**
- **FastAPI**
- **Streamlit**
- **pdfminer.six** for PDF to text conversion
- **Uvicorn** as the ASGI server for running FastAPI

## Getting Started

### Setup
1. Fork or clone this repository to begin working on your solution.
2. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the FastAPI server by navigating to the project directory and running:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Open a new terminal window and launch the Streamlit interface:
   ```bash
   streamlit run streamlit_app.py
   ```
5. Click on Browse files and then upload a PDF file.
6. Click on Convert you will see the extracted texts from the PDF.

### Project Structure
- `app/`: Contains the FastAPI application.
  - `main.py`: The entry point for the FastAPI app.
  - `pdf_to_text.py`: Module responsible for handling PDF file uploads and converting them to text.
- `tests/`: Contains tests to test the feature
  - `test_main.py` : Contains unittests
  - `test.pdf` : Test PDF file
- `streamlit_app.py`: Script for the Streamlit frontend application.
- `requirements.txt`: Specifies project dependencies.

### Unit Test
1. Run the below command under root directory:
   ```bash
   python -m unittest
   ```