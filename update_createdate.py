import os
import subprocess
from datetime import datetime

def update_creation_date(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                filepath = os.path.join(root, file)
                result = subprocess.run(['exiftool', '-DateTimeOriginal', '-s', '-s', '-s', filepath],
                                        stdout=subprocess.PIPE, text=True)
                date_str = result.stdout.strip()
                
                if date_str:
                    date = datetime.strptime(date_str, '%Y:%m:%d %H:%M:%S')
                    os.utime(filepath, (date.timestamp(), date.timestamp()))
                    print(f'Updated creation date for {filepath}')

# Example usage
directory = '/Users/carolinanilsson_r2/Documents/screenshottry'
update_creation_date(directory)
