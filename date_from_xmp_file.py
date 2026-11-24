import os
import subprocess
from datetime import datetime
import xml.etree.ElementTree as ET

def get_date_from_xmp(xmp_path):
    tree = ET.parse(xmp_path)
    root = tree.getroot()
    # Find the DateTimeOriginal field (adjust the namespace as needed)
    date_str = None
    for elem in root.iter():
        if 'DateTimeOriginal' in elem.tag:
            date_str = elem.text
            break
    return date_str

def update_creation_date(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                filepath = os.path.join(root, file)
                xmp_path = os.path.splitext(filepath)[0] + '.xmp'
                
                if os.path.exists(xmp_path):
                    date_str = get_date_from_xmp(xmp_path)
                    
                    if date_str:
                        date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')
                        os.utime(filepath, (date.timestamp(), date.timestamp()))
                        print(f'Updated creation date for {filepath} using {xmp_path}')
                else:
                    print(f'No XMP file found for {filepath}')

# Example usage
directory = '/Users/carolinanilsson_r2/Documents/screenshottry'
update_creation_date(directory)
