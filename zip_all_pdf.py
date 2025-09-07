# zip_all_pdf.py
# Version: 1.1.1
# Date: 2025-08-20
# Author: Bhawesh Tank

import os
import zipfile
import datetime

# ANSI Escape Codes for Colors
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0m'  # Resets all formatting


def main() -> None:
    authentication = authenticate_user("Please Enter the password to login.\nPassword:")
    if authentication:
        # User confirmation
        user_input: str = input(f"{YELLOW}Do you want to zip all .pdf files? (Y/n){RESET}")
        if user_input.lower() == "y":  # Checking user input
            total_zipped_files = zip_files()  # Calling function
            print(f"{GREEN}{total_zipped_files} file(s){RESET} zipped successfully.")
            print(f"Location: {os.getcwd()}")
            exit()
    else:
        print(f"{RED}Invalid Password.\nPlease rerun script again.{RESET}")
        exit()


def authenticate_user(prompt) -> bool:
    password = input(f"{prompt}")
    # Checking password
    if password == datetime.datetime.today().strftime('%H%d%m'):
        return True
    else:
        return False


def zip_files() -> int:
    base_folder = os.getcwd()  # Storing file's current location
    skip_dirs = {"venv", "__pycache__", ".idea"}  # Declaring directories to skip

    files_to_zip = []  # Defining a blank list

    for root, dirs, files in os.walk(base_folder):
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        for file in files:
            if file.lower().endswith(".pdf"):
                file_path = os.path.join(root, file)
                files_to_zip.append(file_path)  # Appending files to list

    with zipfile.ZipFile('data.zip', 'w') as zipf:
        for file in files_to_zip:
            zipf.write(file)

    return len(files_to_zip)


if __name__ == '__main__':
    main()
