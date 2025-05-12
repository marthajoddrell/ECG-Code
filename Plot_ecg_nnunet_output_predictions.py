import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def plot_images(original_image_path, gt_segmentation_path, predicted_segmentation_path, threshold=0.001):
    # Read the images
    original_image = mpimg.imread(original_image_path)
    gt_segmentation = mpimg.imread(gt_segmentation_path)
    predicted_segmentation = mpimg.imread(predicted_segmentation_path)
    
    # Ensure predicted segmentation is in the correct range and data type
    print(f"Data type of predicted segmentation: {predicted_segmentation.dtype}")
    print(f"Shape of predicted segmentation: {predicted_segmentation.shape}")
    
    # Check the unique values in the predicted segmentation before thresholding
    print(f"Unique values in predicted segmentation before thresholding: {np.unique(predicted_segmentation)}")
    
    # Convert predicted segmentation to binary (black and white) with a small threshold
    binary_predicted_segmentation = (predicted_segmentation > threshold).astype(np.uint8)
    
    # Check unique values after thresholding to ensure binary conversion
    print(f"Unique values in binary predicted segmentation: {np.unique(binary_predicted_segmentation)}")
    
    # Plot the original image
    fig, ax = plt.subplots(1, 1, figsize=(5, 5))
    ax.imshow(original_image, cmap='gray')
    ax.set_title("Original Image")
    ax.axis('off')  # Hide axis
    plt.show()

    # Create a figure with 3 subplots
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # Plot the original image
    axes[0].imshow(original_image, cmap='gray')
    axes[0].set_title("Original Image")
    axes[0].axis('off')  # Hide axis
    
    # Plot the ground truth segmentation map
    axes[1].imshow(gt_segmentation, cmap='jet', alpha=0.6)
    axes[1].set_title("Segmentation Map")
    axes[1].axis('off')  # Hide axis
    
    # Plot the predicted segmentation map (binary)
    axes[2].imshow(binary_predicted_segmentation, cmap='gray', vmin=0, vmax=1)
    axes[2].set_title("Predicted Segmentation")
    axes[2].axis('off')  # Hide axis
    
    # Show the plot
    plt.tight_layout()
    plt.show()

# Example usage
original_image_path = '/mnt/wwn-0x50014ee26ba13bde-part2/nnUNet_draft_2/round1_transformations/nnUNet_raw/Dataset201_ECGs/imagesTr/ECG_000000_0000.png'
gt_segmentation_path = '/mnt/wwn-0x50014ee26ba13bde-part2/nnUNet_draft_2/round1_transformations/nnUNet_raw/Dataset201_ECGs/labelsTr/ECG_000000.png'
predicted_segmentation_path = '/mnt/wwn-0x50014ee26ba13bde-part2/nnUNet_draft_2/round1_transformations/nnUNet_results/Dataset201_ECGs/nnUNetTrainer__nnUNetPlans__2d/crossval_results_folds_0_1_2_3_4/ECG_000000.png'

plot_images(original_image_path, gt_segmentation_path, predicted_segmentation_path)
