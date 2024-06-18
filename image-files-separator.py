import os
import shutil
import functions as f


def main():

    SOURCE_PATH = 'images'
    EXTENSIONS = ['CR3', 'JPG']
    TARGET_PATH = 'final_images'

    COPY = True

    EXTENSIONS_DICTIONARY = dict()

    EXTENSIONS_DICTIONARY = f.fill_dictionary(EXTENSIONS, EXTENSIONS_DICTIONARY, TARGET_PATH)

    f.create_folders(EXTENSIONS_DICTIONARY.values())

    files = os.listdir(SOURCE_PATH)

    names_set = set()

    for file in files:

        file_path = f.get_full_file_path(SOURCE_PATH, file)

        extension = f.get_extension(file)

        if COPY:

            shutil.copy(file_path, EXTENSIONS_DICTIONARY[extension])
        
        else:
            
            shutil.move(file_path, EXTENSIONS_DICTIONARY[extension])
        




if __name__ == "__main__":
    main()