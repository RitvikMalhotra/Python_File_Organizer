import os
import shutil
from datetime import datetime

# File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Programs": [".py", ".c", ".cpp", ".java"],
    "Executables": [".exe"],
    "Archives": [".zip", ".rar"]
}


LOG_FILE = "activity_log.txt"


def log_action(message):
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} - {message}\n")


def organize_files(target_folder):
    if not os.path.exists(target_folder):
        print("❌ Folder does not exist.")
        return

    for filename in os.listdir(target_folder):
        file_path = os.path.join(target_folder, filename)

        # Process only files
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False

            for folder, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    folder_path = os.path.join(target_folder, folder)

                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)

                    shutil.move(file_path, os.path.join(folder_path, filename))
                    log_action(f"Moved {filename} to {folder}")
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(target_folder, "Others")
                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)

                shutil.move(file_path, os.path.join(other_folder, filename))
                log_action(f"Moved {filename} to Others")

    print("✅ Files organized successfully!")


def main():
    print("=== Python File Organizer ===")
    target_folder = input("Enter the full path of the folder to organize: ").strip()

    organize_files(target_folder)


if __name__ == "__main__":
    main()
