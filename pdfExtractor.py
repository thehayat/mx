import json
import os.path
import traceback

import PyPDF2
import pdfplumber
from utils import create_folder_if_not_exists


# class PDFReader:
#     def __init__(self, file_path,**kwargs):
#         self.file_path = file_path
#         self.kwargs = kwargs
# 
#     def read_text(self):
#         try:
#             with open(self.file_path, 'rb') as file:
#                 pdf_reader = PyPDF2.PdfReader(file)
#                 text = ''
#                 for page_num in range(len(pdf_reader.pages)):
#                     page = pdf_reader.pages[page_num]
#                     text += page.extract_text()
#                 return text
#         except FileNotFoundError:
#             print(f"File '{self.file_path}' not found.")
#             return None
#         except Exception as e:
#             print(f"An error occurred: {e}")
#             return None


class PDFProcessor:
    def __init__(self, file_path, **kwargs):
        self.file_path = file_path
        self.pdf = pdfplumber.open(file_path)
        self.uuid = kwargs.get("uuid")

    def extract_text(self):
        """Extracts text from all pages of the PDF."""
        extracted_text = {}
        for i, page in enumerate(self.pdf.pages):
            extracted_text[i + 1] = page.extract_text()

        return json.dumps(extracted_text)

    def extract_tables(self):
        """Extracts tables from all pages of the PDF."""
        extracted_tables = {}
        for i, page in enumerate(self.pdf.pages):
            tables = page.extract_tables()
            if tables:
                extracted_tables[i + 1] = tables
        return json.dumps(extracted_tables)

    def extract_images(self):
        """Extracts images from all pages of the PDF."""
        extracted_images = {}
        for i, page in enumerate(self.pdf.pages):
            images = page.images
            if images:
                extracted_images[i + 1] = images
        return extracted_images

    # @create_folder_if_not_exists
    def save_processed(self, path, data):
        """

        :param path:
        :param data:
        :return:
        """
        try:
            dirname = os.path.dirname(path)
            if not os.path.exists(dirname):
                os.makedirs(dirname)
            with open(path, 'w') as fp:
                fp.write(data)
        except Exception:
            print(f"Failed to save.\n {traceback.print_exc()}")
        print(f"Data saved to: {path}")

    def process(self):
        extracted_text = self.extract_text()
        self.save_processed(
            path=os.path.join("processed_folder", self.uuid, "raw_text.json"),
            data=extracted_text
        )

        extracted_tables = self.extract_tables()
        self.save_processed(
            path=os.path.join("processed_folder", self.uuid, "raw_tables.json"),
            data=extracted_tables
        )

        extracted_images = self.extract_images()
        for img_num, img in extracted_images.items():
            self.save_processed(
                path=os.path.join("processed_folder", self.uuid, f"raw_{1}.jpeg"),
                data=img
            )



    def close(self):
        """Closes the PDF file."""
        self.pdf.close()


# Example usage:


# Example usage:
if __name__ == "__main__":
    # pdf_reader = PDFReader("sample1.pdf")
    # # text = pdf_reader.read_text()
    # if text:
    #     print("From pyPDF2", len(text.split()))

    pdf_extractor = PDFProcessor("sample1.pdf")

    # Extract text
    pdf_extractor.process()
    # print("From pdf plumber", len(extracted_tables))

    # Close the PDF file
    pdf_extractor.close()
