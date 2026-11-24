import os
import logging
from datetime import datetime

# Set up logging
log_file = 'duplicate_files_log.txt'
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

# Function to find files with the same ending and creation date
def find_files_with_same_ending_and_date(filename, folder_path):
    filename_ending = filename.split(".")[-1]
    filename_creation_date = os.path.getctime(filename)

    matching_files = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(filename_ending):
                file_path = os.path.join(root, file)
                file_creation_date = os.path.getctime(file_path)

                if file_path != filename:
                    if filename_creation_date == file_creation_date:
                        matching_files.append((file_path, "SAME DATE"))
                    else:
                        matching_files.append((file_path, "DIFFERENT DATE"))

    return matching_files

# Function to scan a folder and log duplicate files
def scan_folder_for_duplicates(folder_path):
    total_space_savings = 0

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            source_file = os.path.join(root, file)
            duplicates = find_files_with_same_ending_and_date(source_file, folder_path)

            if duplicates:
                file_size_mb = os.path.getsize(source_file) / (1024 * 1024)
                logging.info(f'File: {source_file}, Size: {file_size_mb:.2f} MB')
                logging.info('Duplicates:')
                
                for dup_file, status in duplicates:
                    dup_file_size_mb = os.path.getsize(dup_file) / (1024 * 1024)
                    logging.info(f'  {dup_file} - {status}, Size: {dup_file_size_mb:.2f} MB')
                    
                    if status == "SAME DATE":
                        total_space_savings += dup_file_size_mb

    logging.info(f'Total potential space savings: {total_space_savings:.2f} MB')

# Specify the folder to scan
folder_to_scan = '/Volumes/X9 Pro/xxx-new_photosA'
scan_folder_for_duplicates(folder_to_scan)

print(f'Scan complete. Check the log file: {log_file}')
