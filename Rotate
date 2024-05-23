from PIL import Image
import os
import random

# Define range of rotation
def rotate_image(image_path, output_path, rotation_range=(-5, 5)):
    # Open the image
    image = Image.open(image_path)
    
    # Generate a random rotation angle within the specified range
    rotation_angle = random.uniform(rotation_range[0], rotation_range[1])
    
    # Rotate the image without expanding
    rotated_image = image.rotate(rotation_angle, expand=False)
    
    # Handle transparency if the image has an alpha channel
    if 'A' in rotated_image.getbands():
        # Create a new image with white background
        new_image = Image.new("RGBA", rotated_image.size, (255, 255, 255, 255))
        
        # Paste the rotated image onto the new image
        new_image.paste(rotated_image, (0, 0), rotated_image)
        
        # Convert to RGB
        rotated_image = new_image.convert("RGB")
    
    # Save the rotated image
    rotated_image.save(output_path)

# Function to get 10% of .png images in a folder and rotate them
def rotate_10_percent_images(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    
    # Filter .png images
    png_images = [file for file in files if file.endswith('.png')]

    # Calculate 10% of total png images
    num_images_to_rotate = int(len(png_images) * 0.1)

    # Randomly select 10% of the images and rotate them
    images_to_rotate = random.sample(png_images, num_images_to_rotate)

    # Rotate selected images
    for image_file in images_to_rotate:
        image_path = os.path.join(folder_path, image_file)
        output_path = os.path.join(folder_path, f"{image_file}")
        rotate_image(image_path, output_path)

# Example usage:
folder_path = "/Downloads/phsyionet-PRECISE/Transform_Images_with_background"
rotate_10_percent_images(folder_path)
