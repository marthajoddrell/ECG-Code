from PIL import Image

def change_non_white_to_black(image_path, output_path):
    # Open the image
    image = Image.open(image_path)
    image = image.convert("RGBA")  # Ensure the image is in RGBA mode
    
    # Load pixel data
    pixels = image.load()
    
    # Process each pixel
    for y in range(image.height):
        for x in range(image.width):
            r, g, b, a = pixels[x, y]
            # Check if the pixel is not white
            if (r, g, b) != (255, 255, 255):
                # Change to black
                pixels[x, y] = (0, 0, 0, a)
    
    # Save the modified image
    image.save(output_path)

# Example usage
change_non_white_to_black('/Downloads/A/JS00001_2.png', '/Downloads/A/A.png')
