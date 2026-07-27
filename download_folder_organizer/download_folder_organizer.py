import os
import shutil

# Path to Downloads folder
DOWNLOADS = os.path.join(os.path.expanduser("~"), "Downloads")

# File categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programs": [".exe", ".msi", ".apk", ".deb", ".dmg"],
}

# Create category folders
for folder in FILE_TYPES.keys():
    os.makedirs(os.path.join(DOWNLOADS, folder), exist_ok=True)

os.makedirs(os.path.join(DOWNLOADS, "Others"), exist_ok=True)

# Organize files
for file in os.listdir(DOWNLOADS):
    file_path = os.path.join(DOWNLOADS, file)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    extension = os.path.splitext(file)[1].lower()
    moved = False

    for folder, extensions in FILE_TYPES.items():
        if extension in extensions:
            destination = os.path.join(DOWNLOADS, folder, file)
            shutil.move(file_path, destination)
            print(f"Moved: {file} -> {folder}")
            moved = True
            break

    if not moved:
        destination = os.path.join(DOWNLOADS, "Others", file)
        shutil.move(file_path, destination)
        print(f"Moved: {file} -> Others")

print("\nDownload folder organized successfully!")