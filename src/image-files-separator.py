import os
import shutil

from PhotoManager import PhotoManager

from logger import set_logger


set_logger()


def main():

    SOURCE_PATH = 'images'
    TARGET_PATH = 'final_images'
    COPY = True

    photomanager = PhotoManager(SOURCE_PATH, TARGET_PATH, COPY)


    EXTENSIONS_DICTIONARY = dict()

    EXTENSIONS_DICTIONARY = photomanager.fill_dictionary(photomanager.EXTENSIONS, EXTENSIONS_DICTIONARY, TARGET_PATH)

    photomanager.create_folders(EXTENSIONS_DICTIONARY.values())

    files = os.listdir(SOURCE_PATH)

    names_set = set()

    for file in files: 

        file_path = photomanager.get_full_file_path(SOURCE_PATH, file)

        extension = photomanager.get_extension(file)

        if photomanager.COPY:

            shutil.copy(file_path, EXTENSIONS_DICTIONARY[extension])
        
        else:
            
            shutil.move(file_path, EXTENSIONS_DICTIONARY[extension])
        




if __name__ == "__main__":
    main()