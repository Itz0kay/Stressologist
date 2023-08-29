import cv2
import os
import pandas as pd

# Set the path to your image directory
image_dir = 'data/train/'

# Create empty lists to store the image data and folder names
data = []
folders = []

# Loop through each folder in the directory
for folder_name in os.listdir(image_dir):
    # Skip any non-directory files
    if not os.path.isdir(os.path.join(image_dir, folder_name)):
        continue
    # Loop through each image in the folder
    for filename in os.listdir(os.path.join(image_dir, folder_name)):
        # Load the image using OpenCV
        image = cv2.imread(os.path.join(image_dir, folder_name, filename))
        # Flatten the pixel values for each image into a 1D array
        pixels = image.flatten()
        # Append the flattened pixel values and folder name to the data and folders lists
        data.append(pixels)
        folders.append(folder_name)

# Convert the data and folders lists to a pandas DataFrame
df = pd.DataFrame(data)
df['folder'] = folders

# Save the DataFrame to a CSV file
df.to_csv('image_data.csv', index=False)
