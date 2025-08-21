# delete_all_except_pdf.py
# Version: 1.1.1
# Date: 2025-08-20
# Author: Bhawesh Tank

import os
from typing import Tuple
import datetime


def main() -> None:
    authentication = authenticate_user("Please Enter the password to login.\nPassword:")
    if authentication:
        # User confirmation - 1st time
        user_input: str = input("Do you want to delete all files except .pdf. (Y/n)")
        if user_input.lower() == "y":  # Checking user input
            user_input = ""  # Clearing user input

            # User confirmation - 2nd time
            user_input = input("Please confirm again as the data deletion will be irreversible. (Y/n)")
            if user_input.lower() == "y":  # Checking user input
                total_files, deleted_files = delete_dirs()  # Calling function
                print("\nScript executed.\n")
                print(f"Total files: {total_files}")
                print(f"Deleted files: {deleted_files}")
                print(f"Remaining files: {total_files - deleted_files}\n")
                exit()  # Exiting the script

            elif user_input.lower() == "n":
                print("You cancelled the operation in second confirmation.")
            else:
                print("Invalid input. Please enter 'Y' or 'n'.")

        elif user_input.lower() == "n":
            print("You cancelled the operation in first confirmation.")
        else:
            print("Invalid input. Please enter 'Y' or 'n'.")
    else:
        print("Invalid Password.\nPlease rerun script again.")
        exit()


def authenticate_user(prompt) -> bool:
    password = input(f"{prompt}")
    # Checking password
    if password == datetime.datetime.today().strftime('%H%d%m'):
        return True
    else:
        return False


# Function for deleting all *.pdf files from all folders and sub-folders
def delete_dirs() -> tuple[int, int]:
    base_folder = os.getcwd()  # Storing file's current location
    skip_dirs = {"venv", "__pycache__", ".idea"}  # Declaring directories to skip
    total_files, deleted_files = 0, 0  # Creating variable for counting total and deleted files

    for root, dirs, files in os.walk(base_folder):
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        for file in files:
            total_files += 1
            if not file.lower().endswith(".pdf") | file.lower().endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    deleted_files += 1
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")

    return total_files, deleted_files


if __name__ == '__main__':
    main()
