import os
import shutil

def organize_files(directory):
    """
    Organize files in the given directory based on file type.

    Parameters:
        directory (str): Path to the directory to organize.
    """
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return

    # File type categories and their corresponding folders
    file_categories = {
        "Pictures": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
        "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
        "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
        "Code": [".py", ".java", ".cpp", ".js", ".html", ".css"],
        "Others": []
    }

    # Create folders for each category
    for folder in file_categories:
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Organize files
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, ext = os.path.splitext(file)

        # Find the appropriate category
        moved = False
        for category, extensions in file_categories.items():
            if ext.lower() in extensions:
                shutil.move(file_path, os.path.join(directory, category, file))
                moved = True
                break

        # Move files that don't match any category to 'Others'
        if not moved:
            shutil.move(file_path, os.path.join(directory, "Others", file))

    print(f"Files in '{directory}' have been organized.")

def main():
    print("Welcome to the File Organizer!")

    while True:
        choice = input("\nChoose an option:\n1. Organize Files\n2. Exit\n> ").strip()

        if choice == "1":
            directory_to_organize = input("Enter the directory path to organize: ").strip()
            organize_files(directory_to_organize)
        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the program
if __name__ == "__main__":
    main()

