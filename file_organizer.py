import os
import shutil
from datetime import datetime

# Folder to organize (change if needed)
TARGET_FOLDER = "test_folder"

# File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Programs": [".py", ".c", ".cpp", ".java"],
    "Archives": [".zip", ".rar"]
}

LOG_FILE = "activity_log.txt"


def log_action(message):
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} - {message}\n")


def organize_files():
    if not os.path.exists(TARGET_FOLDER):
        print("Target folder not found.")
        return

    for filename in os.listdir(TARGET_FOLDER):
        file_path = os.path.join(TARGET_FOLDER, filename)

        # Process only files
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False

            for folder, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    folder_path = os.path.join(TARGET_FOLDER, folder)

                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)

                    shutil.move(file_path, os.path.join(folder_path, filename))
                    log_action(f"Moved {filename} to {folder}")
                    moved = True
                    break

            # Files with unknown extensions
            if not moved:
                other_folder = os.path.join(TARGET_FOLDER, "Others")

                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)

                shutil.move(file_path, os.path.join(other_folder, filename))
                log_action(f"Moved {filename} to Others")

    print("Files organized successfully!")


if __name__ == "__main__":
    organize_files()
