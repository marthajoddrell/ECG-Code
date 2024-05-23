import os
import random
from PIL import Image

# Path to the folder containing the PNG images
folder_path = "/Downloads/phsyionet-PRECISE/Transform_Images_with_background"

# Get a list of all PNG files in the folder
png_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]

# Calculate 20% of the total number of images
num_images_to_modify = int(0.2 * len(png_files))

# Randomly select 20% of the images
images_to_modify = random.sample(png_files, num_images_to_modify)

# Function to convert background to grayscale at random levels
def convert_background_to_grayscale(image):
    # Open the image
    img = Image.open(os.path.join(folder_path, image))

    # Convert image to RGBA mode if not already in that mode
    img = img.convert('RGBA')

    # Separate the alpha channel
    alpha = img.split()[3]

    # Create a grayscale version of the image
    grayscale = img.convert('L')

    # Randomly adjust brightness level
    brightness_factor = random.uniform(0.5, 1.5)  # Adjust the range as needed
    grayscale = Image.eval(grayscale, lambda x: min(255, max(0, int(x * brightness_factor))))

    # Composite the grayscale image with the original image using the alpha channel
    img = Image.composite(grayscale, img, alpha)

    # Save the modified image
    img.save(os.path.join(folder_path, image))

# Apply the conversion to selected images
for image in images_to_modify:
    convert_background_to_grayscale(image)
