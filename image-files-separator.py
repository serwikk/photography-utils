import os
import functions as f


def main():

    SOURCE_PATH = 'images'
    EXTENSIONS = ['.CR3', '.JPG']
    TARGET_PATH = 'final_images'

    f.create_folders(TARGET_PATH, f.get_folder_names(EXTENSIONS))

    files = os.listdir(SOURCE_PATH)

    names_set = set()

    for file in files:

        file_path = f.get_full_file_path(SOURCE_PATH, file)

        names_set.add(f.remove_extension(file, EXTENSIONS))
        
        if f.is_jpg_file(file_path):

            f.get_shot_date(file_path)





if __name__ == "__main__":
    main()