import os
from collections import defaultdict

# Define the folder path
folder_path = '/Users/carolinanilsson_r2/Library/CloudStorage/OneDrive-Personal/new_photos1/'

# Create a dictionary to store file names by date and original name
file_dict = defaultdict(list)

# Walk through the folder and its subfolders
for root, _, files in os.walk(folder_path):
    for filename in files:
        # Debug statement to show the current file being processed
        print(f'Processing file: {filename}')
        # Extract the date part and the original name part of the filename
        parts = filename.split('_')
        if len(parts) >= 3:
            date_part = parts[0]
            originalname = parts[2]
            # Store the filename in the dictionary with the date and original name as the key
            key = f'{date_part}_{originalname}'
            file_dict[key].append(os.path.join(root, filename))
            print(f'Added file {filename} to key {key}')
        else:
            print(f'Skipped file (wrong format): {filename}')

# Create or overwrite the log file
log_file_path = os.path.join(folder_path, 'duplicates.txt')
try:
    with open(log_file_path, 'w') as log_file:
        # Check for duplicates and write the results to the log file
        for key, files in file_dict.items():
            if len(files) > 1:
                log_file.write(f'Duplicate files found for key {key}:\n')
                for file in files:
                    log_file.write(f'- {file}\n')
                print(f'Duplicate files found for key {key}: {files}')
            else:
                log_file.write(f'No duplicates found for key {key}\n')
                print(f'No duplicates found for key {key}')
    print(f"Duplicates log created at: {log_file_path}")
except IOError as e:
    print(f"Error writing to log file: {e}")

# Add a pause to ensure the final print statement is visible
import time
time.sleep(2)

print("Final contents of file_dict:")
for key, files in file_dict.items():
    print(f"Key: {key}, Files: {files}")
