import os
import shutil

# Source and destination directories
from_dir = "c:/Users/HP EliteBook 840 G4/Downloads"
to_dir = "c:/Users/HP EliteBook 840 G4/Downloads"

# List all files in the source directory
list_of_files = os.listdir(from_dir)
print(list_of_files)

# Function to move files into specific folders based on file type
def move_file(file_name, file_type_folder):
    source_path = os.path.join(from_dir, file_name)
    dest_folder = os.path.join(to_dir, file_type_folder)
    dest_path = os.path.join(dest_folder, file_name)
    
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)  # Create the folder if it doesn't exist
        print(f"Created directory: {dest_folder}")
    
    print(f"Moving {file_name} to {dest_folder}...")
    shutil.move(source_path, dest_path)

# Iterate over each file in the directory
for file_name in list_of_files:
    # Get the file extension (case-insensitive)
    _, extension = os.path.splitext(file_name)
    extension = extension.lower()

    # Skip files without extensions
    if extension == "":
        continue

    # Move images
    if extension in ['.gif', '.png', '.jpg', '.jpeg']:
        move_file(file_name, "imagefiles")

    # You can add more conditions for other file types like:
    # Move documents
    elif extension in ['.pdf', '.docx', '.txt']:
        move_file(file_name, "documentfiles")

    # Move videos
    elif extension in ['.mp4', '.mkv', '.avi']:
        move_file(file_name, "videofiles")

    # Move other files to 'others'
    else:
        move_file(file_name, "others")
