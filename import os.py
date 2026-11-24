import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS

def get_image_info(image_path):
    with Image.open(image_path) as img:
        exif_data = img._getexif()
        if exif_data:
            exif = {TAGS[k]: v for k, v in exif_data.items() if k in TAGS}
            return exif
    return None

def is_screenshot(image_path):
    exif = get_image_info(image_path)
    if exif:
        camera_name = exif.get('Model', '')
        if 'Screenshot' in camera_name:
            return True
    return False

def get_year(image_path):
    exif = get_image_info(image_path)
    if exif:
        date_taken = exif.get('DateTime', '')
        if date_taken:
            return date_taken.split(':')[0]
    return 'Unknown'

def process_folder(folder_path, photo_folder, screenshot_folder):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('jpg', 'jpeg', 'png')):
                file_path = os.path.join(root, file)
                if is_screenshot(file_path):
                    year = get_year(file_path)
                    dest_folder = os.path.join(screenshot_folder, f"{year}_screenshot")
                else:
                    year = get_year(file_path)
                    dest_folder = os.path.join(photo_folder, f"{year}_Photo")
                os.makedirs(dest_folder, exist_ok=True)
                shutil.copy(file_path, os.path.join(dest_folder, file))

# Replace these paths with your actual folder paths
source_folder = '/Users/carolinanilsson_r2/Code/movephotocs/start'
photo_folder = '/Users/carolinanilsson_r2/Code/movephotocs/photos'
screenshot_folder = '/Users/carolinanilsson_r2/Code/movephotocs/screenshots'

process_folder(source_folder, photo_folder, screenshot_folder)
