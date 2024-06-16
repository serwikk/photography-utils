import os
from PIL import Image


def get_full_file_path(folder_path: str, file: str):
    return os.path.join(os.path.abspath(folder_path), file)

def remove_extension(file: str, extensions: list):

    for extension in extensions:
        file = file.replace(extension, '')

    return file


def get_shot_date(file_path: str):

    image = Image.open(file_path)

    exif_data = image._getexif()

    date = exif_data[306]

    print(date)


def is_jpg_file(file_path):
    return ".jpg" in file_path.lower()