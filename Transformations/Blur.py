import cv2
import numpy as np
import os
import random

def blur_image(image, level):
    blurred_image = cv2.blur(image, (level, level))
    return blurred_image

def main():
    # Set the path to your folder of images
    folder_path = "/Downloads/phsyionet-PRECISE/Transform_Images_with_background"

    # Set the output folder
    output_folder = "/Downloads/phsyionet-PRECISE/Transform_Images_with_background"

    # Set the range of levels for blurring
    min_blur_level = 2
    max_blur_level = 4

    # Set the percentage of images to blur
    blur_percentage = 10

    # Get a list of all image files in the folder
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Calculate the number of images to blur
    num_images_to_blur = int(len(image_files) * (blur_percentage / 100))

    # Randomly select images to blur
    images_to_blur = random.sample(image_files, num_images_to_blur)

    for image_file in images_to_blur:
        # Read the image
        image_path = os.path.join(folder_path, image_file)
        image = cv2.imread(image_path)

        # Generate a random blur level
        blur_level = random.randint(min_blur_level, max_blur_level)

        # Apply the blur
        blurred_image = blur_image(image, blur_level)

        # Save the blurred image
        output_path = os.path.join(output_folder, f"{image_file}")
        cv2.imwrite(output_path, blurred_image)

if __name__ == "__main__":
    main()
