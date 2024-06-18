import os
from PIL import Image


def get_full_file_path(folder_path: str, file: str) -> str:

    return os.path.join(os.path.abspath(folder_path), file)


def remove_extension(file: str, extensions: list) -> str:

    for extension in extensions:
        file = file.replace(extension, '')

    return file

def get_extension(file: str) -> str:

    return file.split('.')[-1]


def get_shot_date(file_path: str) -> str:

    image = Image.open(file_path)

    exif_data = image._getexif()

    date = exif_data[306]

    print(date)


def is_jpg_file(file_path) -> bool:
    return ".jpg" in file_path.lower()

def get_folder_names(extensions: list) -> list:

    folder_names = list()

    for extension in extensions:

        folder_names.append(extension.replace('.', ''))

    return folder_names


def create_folders(folder_dictionary):

    for folder_name in folder_dictionary:

        # folder = os.path.join(path, folder_name)    
        os.makedirs(folder_name, exist_ok=True)

def fill_dictionary(values_array, dictionary, path):
    
    for value in values_array:
        dictionary[value] = f'{path}/{value}'

    return dictionary