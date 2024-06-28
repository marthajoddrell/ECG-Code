import os
import random
import shutil

# Define the paths
source_folder = '/home/marthaj/Documents/MAENEW/with'
train_folder = '/home/marthaj/Documents/MAENEW/data/train'
test_folder = '/home/marthaj/Documents/MAENEW/data/test'
val_folder = '/home/marthaj/Documents/MAENEW/data/val'
train_txt = '/home/marthaj/Documents/MAENEW/data/meta/train.txt'
test_txt = '/home/marthaj/Documents/MAENEW/data/meta/test.txt'
val_txt = '/home/marthaj/Documents/MAENEW/data/meta/val.txt'

# Create the destination directories if they don't exist
os.makedirs(train_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)
os.makedirs(val_folder, exist_ok=True)
os.makedirs(os.path.dirname(train_txt), exist_ok=True)

# Get all .png files from the source folder
images = [f for f in os.listdir(source_folder) if f.endswith('.png')]

# Shuffle the list of images
random.shuffle(images)

# Calculate the split indices
total_images = len(images)
train_end = int(0.7 * total_images)
test_end = train_end + int(0.15 * total_images)

# Split the images
train_images = images[:train_end]
test_images = images[train_end:test_end]
val_images = images[test_end:]

# Helper function to move files and write paths to txt files
def move_files_and_write_txt(image_list, destination_folder, txt_file):
    with open(txt_file, 'w') as f:
        for image in image_list:
            src_path = os.path.join(source_folder, image)
            dst_path = os.path.join(destination_folder, image)
            shutil.move(src_path, dst_path)
            f.write(f"{dst_path}\n")

# Move the files and write the paths to the corresponding txt files
move_files_and_write_txt(train_images, train_folder, train_txt)
move_files_and_write_txt(test_images, test_folder, test_txt)
move_files_and_write_txt(val_images, val_folder, val_txt)

print("Images have been split and moved successfully.")
