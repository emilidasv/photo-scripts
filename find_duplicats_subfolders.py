import os
from collections import defaultdict

# Define the folder path
#folder_path = '/Users/carolinanilsson_r2/Documents/testbilder-endastkopior/new_photos/'
folder_path = '/Users/carolinanilsson_r2/Library/CloudStorage/OneDrive-Personal/new_photos1/'


# Create a dictionary to store file names by date and original name
file_dict = defaultdict(list)

# Walk through the folder and its subfolders
for root, _, files in os.walk(folder_path):
    for filename in files:
        # Extract the date part and the original name part of the filename
        parts = filename.split('_')
        if len(parts) >= 3:
            date_part = parts[0]
            originalname = parts[2]
            # Store the filename in the dictionary with the date and original name as the key
            key = f'{date_part}_{originalname}'
            file_dict[key].append(os.path.join(root, filename))

# Create or overwrite the log file
log_file_path = os.path.join(folder_path, 'duplicates.txt')
with open(log_file_path, 'w') as log_file:
    # Check for duplicates and write the results to the log file
    for key, files in file_dict.items():
        if len(files) > 1:
            log_file.write(f'Duplicate files found for key {key}:\n')
            for file in files:
                log_file.write(f'- {file}\n')
        else:
            log_file.write(f'No duplicates found for key {key}\n')

print(f"Duplicates log created at: {log_file_path}")
