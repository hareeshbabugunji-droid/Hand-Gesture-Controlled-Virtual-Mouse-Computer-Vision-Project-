import os
import shutil

folder_path = r"C:\Users\haree\Downloads"

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"],
    "Code_Files": [".py", ".java", ".c", ".cpp", ".html", ".css", ".js"],
}

def organize_files():
    print("\nStarting file organization...")

    # Create category folders
    for category in file_types:
        os.makedirs(os.path.join(folder_path, category), exist_ok=True)

    # Create Others folder
    os.makedirs(os.path.join(folder_path, "Others"), exist_ok=True)

    # Move files
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isdir(file_path):
            continue

        ext = os.path.splitext(file)[1].lower()
        moved = False

        # Try moving safely
        for category, extensions in file_types.items():
            if ext in extensions:
                try:
                    shutil.move(file_path, os.path.join(folder_path, category, file))
                    print(f"Moved: {file} --> {category}")
                except PermissionError:
                    print(f"❌ Skipped (file open): {file}")
                moved = True
                break

        if not moved:
            try:
                shutil.move(file_path, os.path.join(folder_path, "Others", file))
                print(f"Moved: {file} --> Others")
            except PermissionError:
                print(f"❌ Skipped (file open): {file}")

    print("\n✔ File organization complete!")

if __name__ == "__main__":
    organize_files()
