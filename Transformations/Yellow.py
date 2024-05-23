import os
import random
from PIL import Image, ImageEnhance, ImageDraw

# Path to the folder containing the images
folder_path = "/Downloads/phsyionet-PRECISE/Transform_Images_with_background"

# Get a list of all PNG files in the folder
png_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]

# Calculate the number of images to apply the yellow tinge (10%)
num_images_to_modify = int(len(png_files) * 0.1)

# Randomly select images to modify
images_to_modify = random.sample(png_files, num_images_to_modify)

# Function to add yellow tinge at different brightness levels
def add_yellow_tinge(image_path):
    img = Image.open(os.path.join(folder_path, image_path))
    width, height = img.size
    
    # Create a yellow overlay with random transparency
    transparency = random.randint(30, 150)  # Random transparency level between 25% and 75%
    yellow_overlay = Image.new('RGBA', (width, height), (255, 255, 0, transparency))
    
    # Resize the overlay if dimensions don't match
    if img.size != yellow_overlay.size:
        yellow_overlay = yellow_overlay.resize(img.size)
    
    # Apply the overlay to the image
    img_with_yellow = Image.alpha_composite(img.convert('RGBA'), yellow_overlay)
    
    # Save the modified image
    img_with_yellow.save(os.path.join(folder_path, image_path))

# Apply yellow tinge to randomly selected images
for image_file in images_to_modify:
    add_yellow_tinge(image_file)
