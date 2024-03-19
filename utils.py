from datetime import datetime
from functools import wraps
import uuid
import os
def get_uuid():
    current_datetime = datetime.now()
    formatted_date = current_datetime.strftime("%d-%m-%Y")
    new_uuid = uuid.uuid4().hex
    return f"{formatted_date}_{new_uuid}"


def create_folder_if_not_exists(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        folder_path = kwargs.get('path')
        base_dir  = os.path.basename(folder_path)
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        return func(self, *args, **kwargs)
    return wrapper