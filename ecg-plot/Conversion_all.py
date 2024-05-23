import os
from scipy.io import loadmat
import numpy as np
import ecg_plot
import math

# Directory where the .mat files are located
folder_path = '/physionet/files/challenge-2021/1.0.3/training/st_petersburg_incart/All'

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".mat"):
        try:
        # Load ECG data from the current .mat file
            file_path = os.path.join(folder_path, filename)
            mat_data = loadmat(file_path)

        # Assuming the ECG data is stored under the key 'ECG' in the .mat file
            ecg_data = mat_data['val']  # Replace 'ECG' with the actual variable name in your file

        # Find the minimum and maximum values in the array
            min_val = np.min(ecg_data)
            max_val = np.max(ecg_data)

        # Rescale the values to the range [-1, 1]
            scaled_data = 2 * ((ecg_data - min_val) / (max_val - min_val)) - 1
            
            # Remove excess columns to make the number of columns divisible by 1250
            num_columns = scaled_data.shape[1]
            remainder = num_columns % 1250
            if remainder != 0:
                scaled_data = scaled_data[:, :-remainder]

        # Plotting code for each processed file
            shape = ecg_data.shape
            n = shape[1]
            m = n / 1250
            rounded_m = math.floor(m)

        # Reshape the array to match the split dimensions
            reshaped_data = scaled_data.reshape(12, rounded_m, -1)  # Automatically calculate the last dimension
        # Splitting the original array into 'm' separate arrays
            separate_arrays = []
            for i in range(rounded_m):
                separate_arrays.append(reshaped_data[:, i, :])
        # Assigning separate arrays to individual variables
            for i, arr in enumerate(separate_arrays):
                globals()[f'array_{i + 1}'] = arr

            fourth = scaled_data[6, :]
        # Splitting the array into smaller arrays of size (1250,)
            split_arrays = np.array_split(fourth, m)

        # Naming the split arrays as fourth1, fourth2, ..., fourthb
            for i, arr in enumerate(split_arrays, 1):
                exec(f"fourth{i} = arr")

        # Storing split arrays in a list called fourth_arrays
            fourth_arrays = []
            for arr in split_arrays:
                fourth_arrays.append(arr)

            m = int(m)
            num_arrays = m
            num_fourths = m

            final_arrays = []

            for i in range(1, num_arrays + 1):
                current_array = globals()[f"array_{i}"]  # Get array_i dynamically using globals()
                final_array = np.vstack(
                    tuple([current_array] + [globals()[f"fourth{j}"] for j in range(1, num_fourths + 1)])
            )
                final_arrays.append(final_array)
                globals()[f"final_array{i}"] = final_array  # Assign to dynamically named variable
            
            # Plot and save each final_array with a distinct name
                plot_title = f""
                filename_without_extension = os.path.splitext(filename)[0]  # Remove .mat extension
                plot_filename = f"{filename_without_extension}_{i}"
            ## CHECK THE SAMPLING RATE! ##
                ecg_plot.plot(final_array, title=plot_title, columns=4, lead_order=[0,1,2,12,3,4,5,13,6,7,8,14,9,10,11,15])
                ecg_plot.save_as_png(plot_filename)
            
        except Exception as e:
            print(f"Error processing file {filename}: {str(e)}")
