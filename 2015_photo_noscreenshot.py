import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime

def get_exif_data(image):
    try:
        exif = image._getexif()
        if exif is not None:
            return {TAGS.get(tag, tag): value for tag, value in exif.items()}
    except Exception as e:
        print(f"Error reading EXIF data: {e}")
    return {}

def is_photo(file_path):
    try:
        with Image.open(file_path) as img:
            img.verify()  # Check if it's an image
            return True
    except (IOError, SyntaxError) as e:
        print(f"File is not a valid image: {e}")
    return False

def process_folder(folder):
    counter = 0
    for root, _, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            if is_photo(file_path) and 'screenshot' not in file.lower():
                with Image.open(file_path) as img:
                    exif_data = get_exif_data(img)
                    creation_date = exif_data.get('DateTimeOriginal')
                    if creation_date:
                        date = datetime.strptime(creation_date, '%Y:%m:%d %H:%M:%S')
                        if date.year == 2015:
                            new_folder = os.path.join(folder, '2015')
                            os.makedirs(new_folder, exist_ok=True)
                            counter += 1
                            new_name = f"{date.strftime('%Y%m%d')}_{counter:03d}_{file}"
                            new_path = os.path.join(new_folder, new_name)
                            shutil.copy2(file_path, new_path)
                            print(f"Copied {file_path} to {new_path}")

if __name__ == "__main__":
    #/Users/carolinanilsson_r2/Documents/test_bilder
    folder_path = input("Enter the path to the folder: ")
    process_folder(folder_path)
