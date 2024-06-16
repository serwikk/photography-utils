import os
import functions as f


def main():

    SOURCE_PATH = 'images'
    EXTENSIONS = ['.CR3', '.JPG']
    DESTINATION_PATH = 'final_images'

    folder_cr3 = os.path.join(DESTINATION_PATH, 'CR3')
    folder_jpg = os.path.join(DESTINATION_PATH, 'JPG')

    os.makedirs(folder_cr3, exist_ok=True)
    os.makedirs(folder_jpg, exist_ok=True)

    files = os.listdir(SOURCE_PATH)

    names_set = set()

    for file in files:

        file_path = f.get_full_file_path(SOURCE_PATH, file)

        names_set.add(f.remove_extension(file, EXTENSIONS))
        
        if f.is_jpg_file(file_path):

            f.get_shot_date(file_path)


if __name__ == "__main__":
    main()