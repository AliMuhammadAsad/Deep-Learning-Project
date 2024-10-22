import os
import shutil

def batch_images(directory, batch_size):
    # Get the list of .jpg files in the directory
    images = [f for f in os.listdir(directory) if f.endswith('.jpg')]
    images.sort()  # Sort the files to ensure they're in order

    # Create batches and move files
    for i in range(0, len(images), batch_size):
        batch = images[i:i + batch_size]
        folder_name = os.path.join(directory, f"folder{(i // batch_size) + 1}")
        os.makedirs(folder_name, exist_ok=True)
        for image in batch:
            shutil.move(os.path.join(directory, image), os.path.join(folder_name, image))

# Parameters
directory = '.'  # Replace with the path to your directory
batch_size = 20

# Run the function
batch_images(directory, batch_size)
