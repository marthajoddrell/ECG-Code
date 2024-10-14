from PIL import Image
import numpy as np

# Load the image
image_path = '/home/martha/Downloads/ECG_000002.png'
image = Image.open(image_path)

# Convert the image to a NumPy array
image_array = np.array(image)

# Replace all pixel values of 1 with 255
image_array[image_array == 1] = 255

# Convert the NumPy array back to an image
modified_image = Image.fromarray(image_array)

# Save the modified image
modified_image.save('modified_image.png')

print("Pixels with value 1 have been replaced by 255.")


#######################

import matplotlib.pyplot as plt
import numpy as np

# Load the probability map (assuming it's saved as a .npy file)
prob_map = np.load('/home/martha/Downloads/probabilities.npy')

# Check the shape of the probability map
print(f"Original shape: {prob_map.shape}")

# Select one probability map (e.g., for the first class) and squeeze the extra dimensions
prob_map_2d = np.squeeze(prob_map[0, 0, :, :])  # Selecting the first class (index 0)

# Check the new shape
print(f"Squeezed shape: {prob_map_2d.shape}")

# Plot the probability map
plt.imshow(prob_map_2d, cmap='hot')  # 'hot' gives a heatmap-like visualization
plt.colorbar(label='Probability')
plt.title('Probability Map')
plt.show()


################################

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load the image
image_path = '/media/martha/6TB/nnUNet/nnUNet_raw/Dataset201_ECGs/imagesTr/ECG_000048_0000.png'
image = mpimg.imread(image_path)

# Display the image
plt.imshow(image)
plt.axis('off')  # Hide the axes
plt.title('PNG Image')
plt.show()
