import os
from PIL import Image

# Define the directory containing the images
input_directory = '/Downloads/phsyionet-PRECISE/Images_without_background/chapman_shaoxing'
output_directory = '/Downloads/phsyionet-PRECISE/Images_without_background/chapman_shaoxing'

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Define the crop box (left, upper, right, lower)
left = 51
top = 11
right_offset = 17
bottom_offset = 35

# Iterate through all files in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith('.png'):
        # Construct the full file path
        image_path = os.path.join(input_directory, filename)
        
        # Open the image
        image = Image.open(image_path)
        
        # Define the crop box based on the current image size
        right = image.width - right_offset
        bottom = image.height - bottom_offset
        crop_box = (left, top, right, bottom)
        
        # Crop the image
        cropped_image = image.crop(crop_box)
        
        # Save the cropped image to the output directory with the same name
        cropped_image_path = os.path.join(output_directory, filename)
        cropped_image.save(cropped_image_path)
        
        print(f'Cropped image saved as {cropped_image_path}')
