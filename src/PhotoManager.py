import os
from PIL import Image
import logging


class PhotoManager:

    EXTENSIONS = ['CR3', 'JPG']

    def __init__(self, source_path, target_path, copy):

        self.source_path = source_path
        self.target_path = target_path
        self.copy = copy


    def get_full_file_path(self, file: str) -> str:

        logging.info(os.path.join(os.path.abspath(self.source_path), file))

        return os.path.join(os.path.abspath(self.source_path), file)


    @classmethod
    def remove_extension(cls, file: str) -> str:

        for extension in cls.EXTENSIONS:
            file = file.replace(extension, '')

        return file

    @classmethod
    def get_extension(file: str) -> str:

        return file.split('.')[-1]

    @classmethod
    def get_shot_date(file_path: str) -> str:

        image = Image.open(file_path)

        exif_data = image._getexif()

        date = exif_data[306]

        print(date)


    @classmethod
    def is_jpg_file(file_path) -> bool:
        return ".jpg" in file_path.lower()


    @classmethod
    def get_folder_names(cls) -> list:

        folder_names = list()

        for extension in cls.EXTENSIONS:

            folder_names.append(extension.replace('.', ''))

        return folder_names


    def create_folders(folder_dictionary):

        for folder_name in folder_dictionary:

            os.makedirs(folder_name, exist_ok=True)


    def fill_dictionary(values_array, dictionary, path):
        
        for value in values_array:
            dictionary[value] = f'{path}/{value}'

        return dictionary
    

    def get_dictionary_values(dictionary):
        return dictionary.values()