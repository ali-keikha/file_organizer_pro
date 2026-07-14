import os
import shutil
from pathlib import Path
from datetime import datetime

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

def organize_by_date(folder_addres: str):
    filtered_directory = Path(folder_addres)
    
    for item in filtered_directory.iterdir():
        if not item.is_file():
            continue
        info = item.stat()
        date = datetime.fromtimestamp(info.st_ctime)
        folder_name = date.strftime("%Y-%m")
        file_directory = os.path.join(folder_addres, folder_name)
        item_addres = str(item)
        if not os.path.exists(file_directory):
            os.mkdir(file_directory)
            shutil.move(item_addres, file_directory)
        else:
            shutil.move(item_addres, file_directory)

def organize_by_size(file_addres: str):
    for item in os.listdir(file_addres):
        item_addres = os.path.join(file_addres, item)
        if os.path.isdir(item_addres):
            continue
        file_size = os.path.getsize(item_addres)
        
        file_size = file_size / (1024 * 1024)
        if file_size <= 10:
            dir_addres = os.path.join(file_addres, "small")
            if not os.path.exists(dir_addres):
                os.mkdir(dir_addres)
                shutil.move(item_addres, dir_addres)
            else:
                shutil.move(item_addres, dir_addres)
        
        elif 10 < file_size <= 500:
            dir_addres = os.path.join(file_addres, "medium")
            if not os.path.exists(dir_addres):
                os.mkdir(dir_addres)
                shutil.move(item_addres, dir_addres)
            else:
                shutil.move(item_addres, dir_addres)
        
        elif 500 < file_size <= 10000:
            dir_addres = os.path.join(file_addres, "large")
            if not os.path.exists(dir_addres):
                os.mkdir(dir_addres)
                shutil.move(item_addres, dir_addres)
            else:
                shutil.move(item_addres, dir_addres)


while True:

    if os.path.exists(directory):
        
        if os.path.isdir(directory):
        
            option = int(input("Select Option:\n"
                               "1) File Organize by Type\n"
                               "2) File Organize by Date\n"
                               "3) File Organize by Size\n"
                               "4) Exit\n"))

            if option == 1:
                organize_by_name(directory, FILE_TYPES)
            elif option == 2:
                organize_by_date(directory)
            elif option == 3:
                organize_by_size(directory)
            elif option == 4:
                break
            else:
                print("Ente correct number")

        else:
            print("addres is file addres")
            user_answer = input("try again?y/n")
            if user_answer.lower() == "n":
                break

    else:
        print("Directory not found")
        user_answer = input("try again?y/n")
        if user_answer.lower() == "n":
            break