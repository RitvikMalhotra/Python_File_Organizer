import os
import shutil
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox

# ---------------- FILE LOGIC ----------------
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
        messagebox.showerror("Error", "Folder does not exist.")
        return

    moved = 0
    for filename in os.listdir(target_folder):
        file_path = os.path.join(target_folder, filename)

        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            placed = False

            for folder, extensions in FILE_TYPES.items():
                if ext in extensions:
                    dest = os.path.join(target_folder, folder)
                    os.makedirs(dest, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest, filename))
                    log_action(f"Moved {filename} to {folder}")
                    moved += 1
                    placed = True
                    break

            if not placed:
                dest = os.path.join(target_folder, "Others")
                os.makedirs(dest, exist_ok=True)
                shutil.move(file_path, os.path.join(dest, filename))
                log_action(f"Moved {filename} to Others")
                moved += 1

    messagebox.showinfo("Success", f"Files organized successfully!\nFiles moved: {moved}")

def browse_folder():
    path = filedialog.askdirectory()
    folder_var.set(path)

def start_organizing():
    if not folder_var.get():
        messagebox.showwarning("Warning", "Please select a folder.")
        return
    organize_files(folder_var.get())

# ---------------- UI ----------------
root = tk.Tk()
root.title("File Automation System")
root.geometry("600x350")
root.resizable(False, False)
root.configure(bg="white")

# Outer frame (main box)
outer = tk.Frame(root, bg="white", highlightbackground="black",
                 highlightthickness=2)
outer.place(relx=0.5, rely=0.5, anchor="center", width=520, height=260)

# Title box
title_box = tk.Frame(outer, bg="white", highlightbackground="black",
                     highlightthickness=2)
title_box.place(x=110, y=20, width=300, height=50)

tk.Label(
    title_box,
    text="File Automation System",
    font=("Arial", 16, "bold"),
    bg="white"
).pack(expand=True)

# Folder label
tk.Label(
    outer,
    text="Folder Location:",
    font=("Arial", 12),
    bg="white"
).place(x=40, y=90)

folder_var = tk.StringVar()

folder_entry = tk.Entry(
    outer,
    textvariable=folder_var,
    font=("Arial", 11),
    width=45,
    relief="solid",
    bd=1
)
folder_entry.place(x=40, y=120, height=30)

# Buttons
open_btn = tk.Button(
    outer,
    text="Open Folder",
    font=("Arial", 12),
    width=15,
    command=browse_folder
)
open_btn.place(x=80, y=180, height=40)

organize_btn = tk.Button(
    outer,
    text="Organize",
    font=("Arial", 12),
    width=15,
    command=start_organizing
)
organize_btn.place(x=300, y=180, height=40)

root.mainloop()
