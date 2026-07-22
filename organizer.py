import os
import shutil
from pathlib import Path
from datetime import datetime



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

def organize_by_name(address: str, tag_dict: dict):
    report_dict = {}
    
    for item in os.listdir(address):
     
            _ , file_tag = os.path.splitext(item)
            file_address = os.path.join(address, item)
            
            for key in tag_dict:
                
                tag_list = tag_dict[key]
                dirc = os.path.join(address, key)
                for tag in tag_list:
                    
                    if file_tag.lower() == tag:
                        if key not in report_dict:
                            report_dict[key] = []

                        report_dict[key].append(item)
                        if not os.path.exists(dirc):
                            os.mkdir(dirc)
                            shutil.move(file_address, dirc)
                            break
                        else:
                            shutil.move(file_address, dirc)
                            break
                    
    return report_dict

def organize_by_date(folder_address: str):
    filtered_directory = Path(folder_address)
    
    for item in filtered_directory.iterdir():
        if not item.is_file():
            continue
        info = item.stat()
        date = datetime.fromtimestamp(info.st_ctime)
        folder_name = date.strftime("%Y-%m")
        file_directory = os.path.join(folder_address, folder_name)
        item_address = str(item)
        if not os.path.exists(file_directory):
            os.mkdir(file_directory)
            shutil.move(item_address, file_directory)
        else:
            shutil.move(item_address, file_directory)

def organize_by_size(file_address: str):
    for item in os.listdir(file_address):
        item_address = os.path.join(file_address, item)
        if os.path.isdir(item_address):
            continue
        file_size = os.path.getsize(item_address)
        
        file_size = file_size / (1024 * 1024)
        if file_size <= 10:
            dir_address = os.path.join(file_address, "small")
            if not os.path.exists(dir_address):
                os.mkdir(dir_address)
                shutil.move(item_address, dir_address)
            else:
                shutil.move(item_address, dir_address)
        
        elif 10 < file_size <= 500:
            dir_address = os.path.join(file_address, "medium")
            if not os.path.exists(dir_address):
                os.mkdir(dir_address)
                shutil.move(item_address, dir_address)
            else:
                shutil.move(item_address, dir_address)
        
        elif 500 < file_size <= 10000:
            dir_address = os.path.join(file_address, "large")
            if not os.path.exists(dir_address):
                os.mkdir(dir_address)
                shutil.move(item_address, dir_address)
            else:
                shutil.move(item_address, dir_address)


favorite_folder = ""

while True:

    directory = input("enter directory address:(for favorite address type f) \n").lower()

    if directory == "f":
        if os.path.exists(favorite_folder):
            
            if os.path.isdir(favorite_folder):
            
                while True:
                    try:
                        option = int(input("Select Option:\n"
                                "1) File Organize by Type\n"
                                "2) File Organize by Date\n"
                                "3) File Organize by Size\n"
                                "4) Exit\n"))
                        
                        if not 1 <= option <= 4:
                            print("Please enter number between 1 and 4")
                            continue

                        break

                    except ValueError:
                        print("Please enter valid number")
                                

                if option == 1:
                    final_dict = organize_by_name(favorite_folder, FILE_TYPES)
                    
                    for key in final_dict:
                        length = len(final_dict[key])
                        print(f"{key} : {length}")

                elif option == 2:
                    organize_by_date(favorite_folder)
                elif option == 3:
                    organize_by_size(favorite_folder)
                elif option == 4:
                    break
    
                else:
                    print("Please enter a valid option")

            else:
                print("The selected path is a file, not a directory")
                user_answer = input("try again?y/n")
                if user_answer.lower() == "n":
                    break

        else:
            print("Directory not found")
            user_answer = input("try again?y/n")
            if user_answer.lower() == "n":
                break

    else:
    
        if os.path.exists(directory):
            
            if os.path.isdir(directory):
            
                while True:
                    try:
                        option = int(input("Select Option:\n"
                                "1) File Organize by Type\n"
                                "2) File Organize by Date\n"
                                "3) File Organize by Size\n"
                                "4) Add Favorite Folder\n"
                                "5) Exit\n"))
                        
                        if not 1 <= option <= 5:
                            print("Enter number between 1 and 5")
                            continue

                        break

                    except ValueError:
                        print("Please enter valid number")

                if option == 1:
                    final_dict = organize_by_name(directory, FILE_TYPES)

                    for key in final_dict:
                        length = len(final_dict[key])
                        print(f"{key} : {length}")

                elif option == 2:
                    organize_by_date(directory)
                elif option == 3:
                    organize_by_size(directory)
                elif option == 4:
                    favorite_folder = directory
                else:
                    break
            else:
                print("The selected path is a file, not a directory")
                user_answer = input("try again?y/n")
                if user_answer.lower() == "n":
                    break

        else:
            print("Directory not found")
            user_answer = input("try again?y/n")
            if user_answer.lower() == "n":
                break