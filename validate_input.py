import os
from utils import get_uuid


class Validator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.supported_format = ['.pdf']

    def is_valid_format(self):
        if os.path.isfile(self.file_path):
            _, file_extension = os.path.splitext(self.file_path)
            if file_extension.lower() in self.supported_format:
                return True
        return False

    def process(self):
        if self.is_valid_format():
            return {
                "filepath": self.file_path,
                "type": "pdf",
                "uuid": get_uuid()
            }


