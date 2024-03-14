# Document Text Extractor App Challenge

## Overview
This challenge requires building an application that allows users to upload PDF documents through a Streamlit interface. The backend, developed with FastAPI, processes these uploads by converting the PDFs into plain text. The converted text will then be displayed back to the user within the Streamlit interface.

## Objective
Your goal is to create a seamless end-to-end application that showcases your skills in handling file uploads, integrating FastAPI with Streamlit, and performing PDF to text conversion.

## Requirements
- **Python 3.8+**
- **FastAPI**
- **Streamlit**
- **PyMuPDF (fitz)** or **pdfminer.six** for PDF to text conversion
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

### Project Structure
- `app/`: Contains the FastAPI application.
  - `main.py`: The entry point for the FastAPI app.
  - `pdf_to_text.py`: Module responsible for handling PDF file uploads and converting them to text.
- `streamlit_app.py`: Script for the Streamlit frontend application.
- `requirements.txt`: Specifies project dependencies.

## Challenge Tasks
1. **FastAPI Backend**:
   - Implement an endpoint to receive PDF file uploads.
   - Utilize a library for converting the uploaded PDF documents to plain text.

2. **Streamlit Frontend**:
   - Develop a user interface that allows for PDF file uploads.
   - Display the text extracted from the uploaded PDF.

3. **Integration**:
   - Ensure seamless communication and functionality between the Streamlit frontend and FastAPI backend.

## Evaluation Criteria
- **Functionality**: The app must successfully convert uploaded PDFs to text and display the results.
- **Code Quality**: Code should be clean, well-structured, and easy to maintain.
- **User Experience**: The Streamlit UI should be intuitive and straightforward for users.
- **Documentation**: Your code should be well-documented, and your README.md should clearly explain how to set up and run your application.

## Submission Guidelines
Push your completed solution to a GitHub repository and share the link with us. Your README.md should include:
- Detailed instructions for setting up and running your application.
- An overview of your technical decisions and architecture.
- Any challenges encountered and how you addressed them.

We're excited to see your creative and technical capabilities through this challenge. Good luck!