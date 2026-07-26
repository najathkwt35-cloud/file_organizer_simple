
# File Organizer
# This program sorts files in a folder into different folders
# based on their file type (Images, Documents, Videos, etc.)

import os
import shutil

# Step 1: Ask the user for the folder path
folder_path = input("Enter the folder path you want to organize: ")

# Step 2: Define file types and their extensions
image_files = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp']
document_files = ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.xls', '.pptx', '.ppt', '.csv']
video_files = ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv']
audio_files = ['.mp3', '.wav', '.flac', '.aac', '.m4a']
archive_files = ['.zip', '.rar', '.7z', '.tar', '.gz']
code_files = ['.py', '.java', '.c', '.cpp', '.html', '.css', '.js', '.json']

# Step 3: Get list of all files in the folder
files = os.listdir(folder_path)

# Step 4: Loop through each file and move it to the correct folder
for file_name in files:

    file_path = os.path.join(folder_path, file_name)

    # Skip if it's a folder, not a file
    if os.path.isdir(file_path):
        continue

    # Get the file extension (example: ".jpg")
    file_extension = os.path.splitext(file_name)[1].lower()

    # Decide which category folder this file belongs to
    if file_extension in image_files:
        category = "Images"
    elif file_extension in document_files:
        category = "Documents"
    elif file_extension in video_files:
        category = "Videos"
    elif file_extension in audio_files:
        category = "Audio"
    elif file_extension in archive_files:
        category = "Archives"
    elif file_extension in code_files:
        category = "Code"
    else:
        # Any file type that is not listed above goes here
        category = "Others"

    # Step 5: Create the category folder if it does not exist
    category_folder = os.path.join(folder_path, category)

    if not os.path.exists(category_folder):
        os.makedirs(category_folder)

    # Step 6: Move the file into the category folder
    new_path = os.path.join(category_folder, file_name)
    shutil.move(file_path, new_path)

    print(f"Moved: {file_name} --> {category}")

print("\nAll files have been organized successfully!")
