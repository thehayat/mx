import os.path

from pdfExtractor import PDFProcessor
from validate_input import Validator

# Example usage:


# Example usage:
if __name__ == "__main__":
    filename = "sample3.pdf"
    validator = Validator(filename)
    input_params = validator.process()

    extractor = PDFProcessor(file_path=filename,
                                 **input_params)
    extracted_text = extractor.process()