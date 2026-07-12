import os
import shutil

directory = input("enter directory addres: \n")

FILE_TYPES = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp",
        ".webp", ".svg", ".ico", ".tiff", ".heic"
    ],

    "Videos": [
        ".mp4", ".mkv", ".avi", ".mov",
        ".wmv", ".flv", ".webm", ".mpeg"
    ],

    "Audio": [
        ".mp3", ".wav", ".aac", ".flac",
        ".ogg", ".m4a", ".wma"
    ],

    "Documents": [
        ".pdf", ".doc", ".docx", ".txt",
        ".rtf", ".odt", ".md"
    ],

    "Spreadsheets": [
        ".xls", ".xlsx", ".csv", ".ods"
    ],

    "Presentations": [
        ".ppt", ".pptx", ".odp"
    ],

    "Archives": [
        ".zip", ".rar", ".7z",
        ".tar", ".gz", ".bz2", ".xz"
    ],

    "Code": [
        ".py", ".js", ".ts", ".java",
        ".c", ".cpp", ".cs", ".go",
        ".rs", ".php", ".html", ".css",
        ".json", ".xml", ".yaml", ".yml",
        ".sql", ".sh", ".bat"
    ],

    "Executables": [
        ".exe", ".msi", ".apk",
        ".app", ".deb", ".rpm"
    ],

    "Fonts": [
        ".ttf", ".otf", ".woff", ".woff2"
    ],

    "Disk Images": [
        ".iso", ".img"
    ],

}

def organize_by_name(addres: str, tag_dict: dict):
    for item in os.listdir(addres):
            file_name, file_tag = os.path.splitext(item)
            file_addres = os.path.join(addres, item)
            
            for key in tag_dict:
                tag_list = tag_dict[key]
                dirc = os.path.join(addres, key)
                for tag in tag_list:
                    
                    if file_tag.lower() == tag:
                        if not os.path.exists(dirc):
                            os.mkdir(dirc)
                            shutil.move(file_addres, dirc)
                        else:
                            shutil.move(file_addres, dirc)

if os.path.exists(directory):
    
    if os.path.isdir(directory):
       
        organize_by_name(directory, FILE_TYPES)
                        
        print("done")


    else:
        print("addres is file addres")

else:
    print("Directory not found")