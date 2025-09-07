# rename_folders.py
# Version: 1.0.0
# Date: 2025-09-07
# Author: Bhawesh Tank

import os
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
        # Displaying warning to user
        print(f"""
{RED}--- Warning! ---{RESET}
{YELLOW}This script will rename all the folders in this sub directory.
EPF -> EPFO,
ESI -> ESIC
So proceed with extreme caution.{RESET}
        """)
        user_input: str = input(f"Do you want to continue ? (Y/n)")
        if user_input.lower() == "y":  # Checking user input
            folder_name_old: str = input(
                "\nEnter current folder name (Case Sensitive) you want to rename (eg. EPF, ESI)")
            matching_folders: int = count_folders(folder_name_old)
            folder_name_new: str = input("\nEnter new folder name (eg. EPFO, ESIC)")
            user_input2: str = input(f"\n{CYAN}{matching_folders} folders {RESET}will be renamed "
                                     f"from {CYAN}'{folder_name_old}'{RESET} to {CYAN}'{folder_name_new}'{RESET}."
                                     f"Do you wish to continue ? (Y/n)")
            if user_input2.lower() == "y":  # Checking user input 2
                renamed_folders: int = rename_folders(folder_name_old, folder_name_new)
                print(f"\n{GREEN}{renamed_folders} folders renamed successfully.{RESET}\n")
                exit()
            else:
                print(f"{RED}Operation cancelled by user.{RESET}")
        else:
            print(f"{RED}Operation cancelled by user.{RESET}")
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


def count_folders(folder_name: str) -> int:
    base_folder = os.getcwd()  # Storing file's current location
    skip_dirs = {"venv", "__pycache__", ".idea"}  # Declaring directories to skip
    total_folders, matching_folders = 0, 0  # Variable for counting

    for root, dirs, files in os.walk(base_folder):
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        total_folders += 1

        for d in dirs:
            if d == folder_name:
                matching_folders += 1

    print(f"\n{YELLOW}Total Folders: {total_folders}.")
    print(f"Folders named '{folder_name}': {matching_folders}{RESET}.")
    return matching_folders


def rename_folders(old_folder_name: str, new_folder_name: str) -> int:
    base_folder = os.getcwd()  # Starting directory
    skip_dirs = {"venv", "__pycache__", ".idea"}  # Directories to skip

    renamed_folders = 0

    for root, dirs, files in os.walk(base_folder):
        # Skip specified directories
        dirs[:] = [d for d in dirs if d not in skip_dirs]

        for i, d in enumerate(dirs):
            if d == old_folder_name:
                old_path = os.path.join(root, d)
                new_path = os.path.join(root, new_folder_name)

                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed: {old_path} -> {new_path}")
                    renamed_folders += 1
                    dirs[i] = new_folder_name  # Update the list so os.walk continues into renamed folder
                except Exception as e:
                    print(f"Failed to rename {old_path}: {e}")

    return renamed_folders


if __name__ == '__main__':
    main()
