import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def organize_files(directory):
    if not os.path.exists(directory):
        messagebox.showerror("Error", f"The directory '{directory}' does not exist.")
        return
    
    file_categories = {
        "Pictures": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
        "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
        "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
        "Code": [".py", ".java", ".cpp", ".js", ".html", ".css"],
        "Others": []
    }
    
    for folder in file_categories:
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        
        if os.path.isdir(file_path):
            continue
        
        _, ext = os.path.splitext(file)
        
        moved = False
        for category, extensions in file_categories.items():
            if ext.lower() in extensions:
                shutil.move(file_path, os.path.join(directory, category, file))
                moved = True
                break
        
        if not moved:
            shutil.move(file_path, os.path.join(directory, "Others", file))
    
    messagebox.showinfo("Success", f"Files in '{directory}' have been organized.")

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        organize_files(directory)

def main():
    root = tk.Tk()
    root.title("File Organizer")
    
    tk.Button(root, text="Select Directory to Organize", command=select_directory).pack(pady=20)
    tk.Button(root, text="Exit", command=root.quit).pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
