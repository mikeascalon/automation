from rich.console import Console
from rich.prompt import Prompt
from rich import print as rprint  # Use rich's print for styled text
import os
import shutil


# Initialize a Rich console object
console = Console()

def create_folder(folder_name):
    """Creates a folder with the specified name."""
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created.")
    else:
        print(f"Folder '{folder_name}' already exists.")

def move_user_documents(user_folder, temp_folder):
    """Moves documents from a deleted user's folder to a temporary folder."""
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)
    for file_name in os.listdir(user_folder):
        shutil.move(os.path.join(user_folder, file_name), os.path.join(temp_folder, file_name))
    print(f"Documents moved from {user_folder} to {temp_folder}.")

def sort_documents(folder_path):
    """Sorts documents in the given folder into subfolders based on their file type."""
    log_folder = os.path.join(folder_path, 'logs')
    mail_folder = os.path.join(folder_path, 'mail')
    create_folder(log_folder)
    create_folder(mail_folder)

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.log.txt'):
            shutil.move(os.path.join(folder_path, file_name), log_folder)
        elif file_name.endswith('.mail'):
            shutil.move(os.path.join(folder_path, file_name), mail_folder)
    print("Documents sorted into 'logs' and 'mail' folders.")

def main_menu():
    console.clear()  # Optional: clear the console before displaying the menu
    rprint("[bold cyan]Automation Task Menu:[/bold cyan]")
    rprint("[1] Create a Folder")
    rprint("[2] Move Deleted User's Documents")
    rprint("[3] Sort Documents into Folders")
    rprint("[4] Parse Log File")
    rprint("[5] Backup Specific Folders")
    choice = Prompt.ask("Enter your choice", choices=["1", "2", "3", "4", "5"])

    if choice == '1':
        folder_name = Prompt.ask("Enter the name of the folder to create")
        create_folder(folder_name)
    elif choice == '2':
        user_folder = Prompt.ask("Enter the path of the deleted user's folder")
        temp_folder = Prompt.ask("Enter the path of the temporary folder")
        move_user_documents(user_folder, temp_folder)
    elif choice == '3':
        folder_path = Prompt.ask("Enter the folder path to sort documents")
        sort_documents(folder_path)
    elif choice == '4':
        log_folder = Prompt.ask("Enter the log folder path")
        parse_log_file(log_folder)
    elif choice == '5':
        src_folder = Prompt.ask("Enter the source folder for backup")
        backup_folder = Prompt.ask("Enter the backup folder path")
        backup_folders(src_folder, backup_folder)
    else:
        rprint("[bold red]Invalid choice. Please enter a number between 1 and 5.[/bold red]")

# Make sure to include the other function definitions from the previous script here

if __name__ == "__main__":
    main_menu()
