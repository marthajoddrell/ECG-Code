import os
import shutil

# Define the path to the main folder
main_folder = 'st_petersburg_incart'

# Iterate through each subfolder in the main folder
for subfolder in os.listdir(main_folder):
    subfolder_path = os.path.join(main_folder, subfolder)
    # Check if the subfolder_path is a directory
    if os.path.isdir(subfolder_path):
        # Iterate through each file in the subfolder
        for file in os.listdir(subfolder_path):
            if file.endswith('.mat'):
                file_path = os.path.join(subfolder_path, file)
                # Move the .mat file to the main folder
                shutil.move(file_path, main_folder)

print("All .mat files have been extracted to the 'chapman_shaoxing' folder.")
