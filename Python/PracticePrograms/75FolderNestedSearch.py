# Program: Recursive Folder Scanner
# Real Use Case: Many operating systems & tools scan folders recursively.
# This program lists all files in nested folders.

print("===== RECURSIVE FOLDER SCANNER =====")

def scan_folder(folder, level=0):
    for name, content in folder.items():
        print("  " * level + "- " + name)

        # If value is a dictionary → it's a subfolder → scan again recursively
        if isinstance(content, dict):
            scan_folder(content, level + 1)

# Mock folder structure (dictionary)
filesystem = {
    "Documents": {
        "Resume.pdf": None,
        "Project": {
            "Report.docx": None,
            "Data.xlsx": None
        }
    },
    "Pictures": {
        "Vacation": {
            "img1.jpg": None,
            "img2.jpg": None
        },
        "profile.png": None
    }
}

scan_folder(filesystem)
