import os
import random
import cv2
import numpy as np

def create_darker_ecg_style_v1(image_path, output_path):
    # Step 1: Read the image
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 2: Add noise (less intense)
    noise = np.random.normal(0, 2, gray_image.shape).astype('uint8')
    noisy_image = cv2.add(gray_image, noise)

    # Step 3: Darken the background by 20%
    darkened_image = cv2.multiply(noisy_image, np.array(0.8))

    # Step 4: Save the final image
    cv2.imwrite(output_path, darkened_image)

def create_darker_ecg_style_v2(image_path, output_path):
    # Step 1: Read the image
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 2: Darken the background by 20%
    darkened_image = cv2.multiply(gray_image, np.array(0.6))

    # Step 3: Add noise (lower intensity)
    noise = np.random.normal(0, 1, darkened_image.shape).astype('uint8')
    noisy_image = cv2.add(darkened_image, noise)

    # Step 4: Enhance gridlines and ECG signals
    enhanced_image = cv2.equalizeHist(noisy_image)

    # Step 5: Save the final image
    cv2.imwrite(output_path, enhanced_image)

def process_random_images(input_folder, output_folder, percentage=5):
    # Get a list of all .png files in the folder
    all_images = [f for f in os.listdir(input_folder) if f.endswith('.png')]

    # Calculate the number of images for each transformation
    total_images = len(all_images)
    num_images_to_process = max(1, total_images * percentage // 100)

    # Randomly select unique images for each transformation
    selected_images_v1 = set(random.sample(all_images, num_images_to_process))
    remaining_images = list(set(all_images) - selected_images_v1)
    selected_images_v2 = set(random.sample(remaining_images, num_images_to_process))

    # Apply the first transformation
    for image_name in selected_images_v1:
        input_path = os.path.join(input_folder, image_name)
        output_path = os.path.join(output_folder, f"v1_{image_name}")
        create_darker_ecg_style_v1(input_path, output_path)

    # Apply the second transformation
    for image_name in selected_images_v2:
        input_path = os.path.join(input_folder, image_name)
        output_path = os.path.join(output_folder, f"v2_{image_name}")
        create_darker_ecg_style_v2(input_path, output_path)

    # Copy the unprocessed images to the output folder
    unprocessed_images = set(all_images) - selected_images_v1 - selected_images_v2
    for image_name in unprocessed_images:
        input_path = os.path.join(input_folder, image_name)
        output_path = os.path.join(output_folder, image_name)
        if not os.path.exists(output_path):
            os.makedirs(output_folder, exist_ok=True)
        cv2.imwrite(output_path, cv2.imread(input_path))

# Example usage
input_folder = "/mnt/wwn-0x50014ee26ba13bde-part2/round2_nnUNet/nnUNet_raw/Dataset201_ECGs/imagesTr"  # Replace with your input folder path
output_folder = "/mnt/wwn-0x50014ee26ba13bde-part2/round2_nnUNet/nnUNet_raw/Dataset201_ECGs/imagesTr_new"  # Replace with your output folder path
os.makedirs(output_folder, exist_ok=True)  # Create the output folder if it doesn't exist

process_random_images(input_folder, output_folder, percentage=5)
