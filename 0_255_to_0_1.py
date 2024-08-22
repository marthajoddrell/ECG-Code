from PIL import Image
import os

# Path to the folder containing images
input_folder = '/home/martha/Downloads/nnUNet/nnUNet_raw/Dataset201_ECGs/labelsTr'
output_folder = '/home/martha/Downloads/nnUNet/nnUNet_raw/Dataset201_ECGs/labelsTr'

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith('.png'):
        # Open the image
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path).convert('L')  # Convert to grayscale if not already

        # Load pixel data
        pixels = img.load()

        # Process pixels
        for i in range(img.width):
            for j in range(img.height):
                pixel_value = pixels[i, j]
                if pixel_value == 255:
                    pixels[i, j] = 1
                else:
                    pixels[i, j] = 0

        # Save the modified image
        output_path = os.path.join(output_folder, filename)
        img.save(output_path)

print("Processing complete.")
