import os
import exiftool
from datetime import datetime

def update_creation_date(directory):
    with pyexiftool.ExifTool() as et:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    filepath = os.path.join(root, file)
                    metadata = et.get_metadata(filepath)
                    
                    if 'EXIF:DateTimeOriginal' in metadata:
                        date_str = metadata['EXIF:DateTimeOriginal']
                        date = datetime.strptime(date_str, '%Y:%m:%d %H:%M:%S')
                        
                        # Update file creation date
                        os.utime(filepath, (date.timestamp(), date.timestamp()))
                        print(f'Updated creation date for {filepath}')

# Example usage
directory = '/Users/carolinanilsson_r2/Documents/screenshottry'
update_creation_date(directory)
