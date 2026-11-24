import os

def get_image_size(folder_path):
    total_size = 0
    for dirpath, _, filenames in os.walk(folder_path):
        for file in filenames:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
                file_path = os.path.join(dirpath, file)
                total_size += os.path.getsize(file_path)
    return total_size

# Replace 'your_folder_path' with the path to your folder
#folder_path = 'your_folder_path'
folder_path = '/Volumes/X9 Pro/'
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
total_size_in_bytes = get_image_size(folder_path)

# Convert to MB for easier reading
total_size_in_MB = total_size_in_bytes / (1024 * 1024)
print(f"Total size of all images: {total_size_in_MB:.2f} MB")