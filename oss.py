import shutil
import os

# Define the source and destination paths
source_file = 'C:/Users/Ala/Downloads/audio.wav'
destination_folder = 'C:/Users/Ala/Desktop/gptextra-backend'

# Check if the file already exists in the destination folder
if os.path.isfile(os.path.join(destination_folder, os.path.basename(source_file))):
    # If the file exists, remove it before moving the new one
    os.remove(os.path.join(destination_folder, os.path.basename(source_file)))

# Move the file to the destination folder
shutil.move(source_file, destination_folder)
