import os

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, _, filenames in os.walk(folder_path):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            total_size += os.path.getsize(file_path)
    return total_size

def log_all_subfolders(folder_path, log_file):
    with open(log_file, 'w') as log:
        for dirpath, dirnames, _ in os.walk(folder_path):
            for dirname in dirnames:
                subfolder_path = os.path.join(dirpath, dirname)
                folder_size = get_folder_size(subfolder_path)
                folder_size_in_MB = folder_size / (1024 * 1024)
                log.write(f"{subfolder_path}: {folder_size_in_MB:.2f} MB\n")

# Replace 'your_folder_path' with the path to your folder
#folder_path = 'your_folder_path'
folder_path = '/Volumes/X9 Pro/Carolinas HP dec 2024/' 
#folder_path ='/Volumes/TOSHIBA EXT/lacie/'
#folder_path = '/Volumes/TOSHIBA EXT/'
#sizelog_toshoba
#folder_path = '/Volumes/X9 Pro/' 
#sizelog_copy.txt

#631138.08 MB
#folder_path = '/Volumes/X9 Pro/macbook-backup'
#folder_path = '/Volumes/X9 Pro/macbook-backup'
#102112.94 MB
#folder_path = '/Volumes/X9 Pro/icloud-carolina-photos'
#72912.36 MB
#folder_path = '/Volumes/X9 Pro/green disk'
#231535.40 MB
#folder_path = '/Volumes/X9 Pro//Carolinas HP dec 2024'
#222721.33 MB
#folder_path = '/Volumes/X9 Pro/code' 
#6MB

log_file = 'sizelog.txt'

log_all_subfolders(folder_path, log_file)

print(f"Log file created: {log_file}")