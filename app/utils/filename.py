import uuid
import os

def generate_storage_name(
    filename:str
):

    extension=os.path.splitext(
        filename
    )[1]

    return f"{uuid.uuid4()}{extension}"