import os
import pandas as pd

# Define the path to your folder
folder_path = '/mnt/wwn-0x50014ee26ba13bde-part2/PRECISE_nnUNet/6099_cropped/'

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        
        try:
            # Read the file line-by-line into a list of lists, allowing different row lengths
            with open(file_path, 'r') as file:
                rows = [line.strip().split(',') for line in file]

            # Remove the first column from each row
            rows = [row[1:] for row in rows]

            # Ensure all rows except the last one have 251 columns (padding with NaN if needed)
            for i in range(len(rows) - 1):
                rows[i] = rows[i] + [pd.NA] * (251 - len(rows[i]))  # Pad to 251 columns
            
            # Handle the final row, which should have 1001 columns after removing the first one
            final_row = rows[12] + [pd.NA] * (1001 - len(rows[12]))  # Pad to 1001 columns

            # Split the final row into three new rows
            row_14 = final_row[250:500]
            row_15 = final_row[500:750]
            row_16 = final_row[750:1000]

            # Convert rows back to a DataFrame and add the new rows
            df = pd.DataFrame(rows[:12] + [row_14, row_15, row_16], dtype='object')

            # Save the modified DataFrame back to the original CSV file
            df.to_csv(file_path, header=False, index=False)
        
        except Exception as e:
            print(f"Error reading {filename}: {e}")
