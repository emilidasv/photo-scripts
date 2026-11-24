import os

def verify_path(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        if os.access(path, os.R_OK | os.W_OK):
            print(f"The path '{path}' is accessible for reading and writing.")
        else:
            print(f"The path '{path}' is not accessible for reading and writing.")
    else:
        print(f"The path '{path}' does not exist.")

# Replace with the path you want to verify
folder_path = '/Users/carolinanilsson_r2/Library/CloudStorage/OneDrive-Personal/new_photos1/'
verify_path(folder_path)
