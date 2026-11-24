import os
from collections import defaultdict

# Define the folder path
#folder_path = 'path/to/your/folder'
folder_path = '/Users/carolinanilsson_r2/Documents/testbilder-endastkopior/new_photos/2009_new/'

# Create a dictionary to store file names by date and original name
file_dict = defaultdict(list)

# List all files in the folder
for filename in os.listdir(folder_path):
    # Extract the date part and the original name part of the filename
    parts = filename.split('_')
    if len(parts) >= 3:
        date_part = parts[0]
        originalname = parts[2]
        # Store the filename in the dictionary with the date and original name as the key
        key = f'{date_part}_{originalname}'
        file_dict[key].append(filename)

# Check for duplicates and print the results
for key, files in file_dict.items():
    if len(files) > 1:
        print(f'Duplicate files found for key {key}:')
        for file in files:
            print(f'- {file}')
    else:
        print(f'No duplicates found for key {key}')

# Usage example: replace 'path/to/your/folder' with the actual folder path
#folder_path = '/path/to/your/folder'
