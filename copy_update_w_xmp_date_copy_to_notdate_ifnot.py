import os
import shutil
from datetime import datetime
import xml.etree.ElementTree as ET

def get_date_from_xmp(xmp_path):
    try:
        tree = ET.parse(xmp_path)
        root = tree.getroot()
        namespaces = {
            'photoshop': 'http://ns.adobe.com/photoshop/1.0/'
        }
        date_elem = root.find('.//photoshop:DateCreated', namespaces)
        if date_elem is not None:
            return date_elem.text
    except ET.ParseError as e:
        print(f"Error parsing {xmp_path}: {e}")
    return None

def copy_and_update_creation_date(directory, output_directory, no_date_output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    if not os.path.exists(no_date_output_directory):
        os.makedirs(no_date_output_directory)
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.mp4', '.mov')):
                filepath = os.path.join(root, file)
                xmp_path = os.path.splitext(filepath)[0] + '.xmp'
                
                if os.path.exists(xmp_path):
                    date_str = get_date_from_xmp(xmp_path)
                    
                    if date_str:
                        try:
                            date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S%z')
                            new_filepath = os.path.join(output_directory, file)
                            shutil.copy2(filepath, new_filepath)
                            os.utime(new_filepath, (date.timestamp(), date.timestamp()))
                            print(f'Copied and updated creation date for {new_filepath} using {xmp_path}')
                        except ValueError as e:
                            print(f"Error parsing date for {filepath}: {e}")
                    else:
                        new_filepath = os.path.join(no_date_output_directory, file)
                        shutil.copy2(filepath, new_filepath)
                        print(f'Copied {new_filepath} to no date folder')
                else:
                    new_filepath = os.path.join(no_date_output_directory, file)
                    shutil.copy2(filepath, new_filepath)
                    print(f'Copied {new_filepath} to no date folder')

# Example usage
#directory = '/Users/carolinanilsson_r2/Documents/screenshot'
#output_directory = '/Users/carolinanilsson_r2/Documents/screenshots_copy_update_date_from_xmp'
#no_date_output_directory = '/Users/carolinanilsson_r2/Documents/screenshot_copy_nodate'
#directory = '/Users/carolinanilsson_r2/Documents/finns/screen-recordings'
#output_directory = '/Users/carolinanilsson_r2/Documents//finns/screen-recording_update_date'
#no_date_output_directory = '/Users/carolinanilsson_r2/Documents/finns/screen-recordings_nodate'
directory = '/Users/carolinanilsson_r2/Documents/icloud_mov'
#output_directory = '/Users/carolinanilsson_r2/Documents/icloud_date2'
output_directory = '/Volumes/X9 Pro/icloud-rec_w_date'
no_date_output_directory = '/Users/carolinanilsson_r2/icloud_nodate'
copy_and_update_creation_date(directory, output_directory, no_date_output_directory)
