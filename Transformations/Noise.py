import os
import cv2
import numpy as np
import random

# Function to add noise to an image
def add_noise(image, noise_level):
    # Generate Gaussian noise
    row, col, ch = image.shape
    gauss = np.random.normal(0, noise_level, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy_image = image + gauss
    return noisy_image

# Folder containing .png images
folder_path = "/Downloads/phsyionet-PRECISE/Transform_Images_with_background"
# List all files in the folder
file_list = os.listdir(folder_path)

# Set noise levels range
min_noise_level = 30
max_noise_level = 150

# Calculate how many images should have noise
num_images_with_noise = int(len(file_list) * 0.25)

# Randomly select images to add noise
images_to_add_noise = random.sample(file_list, num_images_with_noise)

# Loop through images
for filename in file_list:
    if filename.endswith(".png"):
        image_path = os.path.join(folder_path, filename)
        
        # Load the image
        image = cv2.imread(image_path)
        
        # Check if this image should have noise added
        if filename in images_to_add_noise:
            # Randomly select noise level
            noise_level = random.randint(min_noise_level, max_noise_level)
            # Add noise to the image
            noisy_image = add_noise(image, noise_level)
            # Save the noisy image
            cv2.imwrite(os.path.join(folder_path,  filename), noisy_image)
        else:
            # If no noise is to be added, simply copy the image
            cv2.imwrite(os.path.join(folder_path, filename), image)
