import os
import shutil
from datetime import datetime
import xml.etree.ElementTree as ET

def get_date_from_xmp(xmp_path):
    try:
        tree = ET.parse(xmp_path)
        root = tree.getroot()
        # Find the Photoshop DateCreated field (adjust the namespace as needed)
        date_str = None
        for elem in root.iter():
            if 'DateCreated' in elem.tag and 'photoshop' in elem.tag:
                date_str = elem.text
                break
        return date_str
    except ET.ParseError as e:
        print(f"Error parsing {xmp_path}: {e}")
        return None

def copy_and_update_creation_date(directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                filepath = os.path.join(root, file)
                xmp_path = os.path.splitext(filepath)[0] + '.xmp'
                
                if os.path.exists(xmp_path):
                    date_str = get_date_from_xmp(xmp_path)
                    
                    if date_str:
                        try:
                            date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')
                            new_filepath = os.path.join(output_directory, file)
                            shutil.copy2(filepath, new_filepath)
                            os.utime(new_filepath, (date.timestamp(), date.timestamp()))
                            print(f'Copied and updated creation date for {new_filepath} using {xmp_path}')
                        except ValueError as e:
                            print(f"Error parsing date for {filepath}: {e}")
                    else:
                        print(f"No valid date found in {xmp_path}")
                else:
                    print(f'No XMP file found for {filepath}')

# Example usage
directory = '/Users/carolinanilsson_r2/Documents/screenshottry'
output_directory = '/Users/carolinanilsson_r2/Documents/screenshottry_copy'
copy_and_update_creation_date(directory, output_directory)
