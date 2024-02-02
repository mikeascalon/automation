
# LAB - Class 19

## Project: Automation

**Author:** Michelangelo Ascalon

### Overview
This project to improve the organization and automation of various tasks. This includes handling user data, sorting files, parsing logs, and other miscellaneous tasks. You’ll be writing Python scripts to automate these tasks and make your team’s work more efficient.

### Setup

#### Dependencies
- Make sure Python is installed on your machine.
- Install necessary Python packages from `requirements.txt` using the command:
  ```bash
  pip install -r requirements.txt
  ```

### How to Run the Application

1. Clone the repository to your local machine.
2. Navigate to the directory containing `automation.py`.
3. Run the script using Python:
   ```bash
   python automation.py
   ```

### How to Use

After running the script, you will be presented with a menu-driven interface that allows you to select from a list of automation tasks:

* **Create a Folder:** Create a new folder by specifying its name. Useful for organizing files into new directories.
  
* **Move Deleted User's Documents:** Move documents from a deleted user's folder to a temporary folder. This helps in archiving or cleaning user data while keeping a record.

* **Sort Documents into Folders:** Automatically sort documents into specified folders based on their file type. For example, log files are moved to a 'logs' folder, and email files to a 'mail' folder.

* **Parse Log File:** Analyze log files for errors and warnings. The script extracts these entries and saves them into separate files for easier troubleshooting. **Still working on this feature**

* **Backup Specific Folders:** Choose a folder to backup and specify a backup destination. The script will copy the contents, preserving the folder structure for security or redundancy purposes **Still working on this feature**

### Features

* **Menu-Driven Interface:** Easy-to-navigate options presented in a clear, structured format thanks to the rich library.

* **Folder Creation:** Streamline the process of making new directories for better file organization.

* **User Data Handling:** Safely move and archive documents from deleted users, ensuring data is not lost during user management processes.

* **Document Sorting:** Automate the categorization of files into appropriate folders, saving time and reducing clutter.

* **Log Parsing:** Quickly identify and isolate errors and warnings from log files, enhancing the troubleshooting process. **Still working on this feature**

* **Data Backup:** Facilitate the backup of critical folders with an easy-to-use option, ensuring data integrity and availability **Still working on this feature**
