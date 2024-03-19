import streamlit as st
import os
import pdfplumber


# Function to extract text from PDF
def extract_text(pdf_path):
    print("Extracting text from PDF...")
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    print("Text extraction completed.")
    return text


# Function to get metadata of PDF
def get_metadata(pdf_path):
    print("Getting metadata of PDF...")
    metadata = {}
    with pdfplumber.open(pdf_path) as pdf:
        metadata['Title'] = pdf.doc.catalog.get("Title", "N/A")
        metadata['Author'] = pdf.doc.catalog.get("Author", "N/A")
        metadata['Number of Pages'] = len(pdf.pages)
    print("Metadata retrieval completed.")
    return metadata


# Path to processed folder
processed_folder = "processed"

# List PDFs in processed folder
pdf_files = [f for f in os.listdir(processed_folder) if f.endswith(".pdf")]

# Sidebar - Dropdown to select PDF
selected_pdf = st.sidebar.selectbox("Select PDF", pdf_files)

# If PDF is selected
if selected_pdf:
    print(f"Selected PDF: {selected_pdf}")
    # Path to selected PDF
    pdf_path = os.path.join(processed_folder, selected_pdf)

    # Extract text from PDF
    pdf_text = extract_text(pdf_path)
    print("PDF text extracted.")

    # Get metadata of PDF
    pdf_metadata = get_metadata(pdf_path)
    print("PDF metadata retrieved.")

    # Display metadata
    st.header("PDF Metadata")
    for key, value in pdf_metadata.items():
        st.write(f"**{key}:** {value}")

    # Display PDF text
    st.subheader("PDF Text")
    st.text(pdf_text)

    # Display PDF file
    st.subheader("PDF Viewer")
    with open(pdf_path, "rb") as f:
        st.write(f.read())
