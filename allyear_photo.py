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

def log_message(message, file_path, log_file_path):
    with open(log_file_path, "a") as log_file:
        log_file.write(f"{message} (File path: {file_path})\n")
    print(f"Log written: {message} (File path: {file_path})")

def process_folder(folder):
    log_file_path = os.path.join(folder, "log.txt")
    new_photos_folder = os.path.join(folder, "new_photos")
    os.makedirs(new_photos_folder, exist_ok=True)
    counters = {}
    for root, _, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            if is_photo(file_path) and 'screenshot' not in file.lower():
                with Image.open(file_path) as img:
                    exif_data = get_exif_data(img)
                    creation_date = exif_data.get('DateTimeOriginal')
                    if creation_date:
                        date = datetime.strptime(creation_date, '%Y:%m:%d %H:%M:%S')
                        year = date.year
                        if year not in counters:
                            counters[year] = 0
                        year_folder = os.path.join(new_photos_folder, f'{year}_new')
                        os.makedirs(year_folder, exist_ok=True)
                        counters[year] += 1
                        new_name = f"{date.strftime('%Y%m%d')}_{counters[year]:03d}_{file}"
                        new_path = os.path.join(year_folder, new_name)
                        shutil.copy2(file_path, new_path)
                        log_message(f"Did copy: {new_name}", file_path, log_file_path)
                        print(f"Copied {file_path} to {new_path}")
                    else:
                        log_message(f"Did not copy: {file} (No EXIF date)", file_path, log_file_path)
            else:
                log_message(f"Did not copy: {file} (Not a photo)", file_path, log_file_path)

    print(f"Log file created at: {log_file_path}")

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder: ")
    process_folder(folder_path)
