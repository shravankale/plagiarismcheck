import zipfile, argparse
import os
import sys, shutil

def remove_resource_forks(target_directory):
    "Removes the __MACOSX folders"

    for root, dirs, files in os.walk(target_directory):
        for name in dirs:
            if '__MACOSX' in name:
                shutil.rmtree(os.path.join(root,name))

def remove_files_with_string(target_directory,exclude_string=None):

    if exclude_string is not None:
        for root, dirs, files in os.walk(target_directory):
            for file in files:
                if exclude_string.lower() in file.lower():
                    os.remove(os.path.join(root,file))

def extract_zip(zip_file, destination_folder):
    """Extract a zip file to the specified destination folder."""
    try:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(destination_folder)
        return True
    except zipfile.BadZipFile:
        return False

def main(root_folder, target_directory, exclude_string=None):
    """Extract all zip files from the root_folder to target_directory."""
    if not os.path.exists(root_folder):
        print(f"Folder '{root_folder}' doesn't exist!")
        return

    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    total_zip_files = 0
    successful_unzips = 0
    unsuccessful_unzips = []

    # Walk through the root folder
    for folder_name, _, file_names in os.walk(root_folder):
        for file_name in file_names:
            if file_name.endswith('.zip'):
                total_zip_files += 1

                zip_path = os.path.join(folder_name, file_name)
                destination_folder = os.path.join(target_directory, file_name[:-4])  # Remove .zip extension

                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                success = extract_zip(zip_path, destination_folder)
                if success:
                    successful_unzips += 1
                    remove_resource_forks(destination_folder)
                    remove_files_with_string(destination_folder,exclude_string)
                else:
                    unsuccessful_unzips.append(zip_path)

    # Save unsuccessful unzip attempts to file
    with open('unzip-error.txt', 'w') as error_file:
        for path in unsuccessful_unzips:
            error_file.write(f"{path}\n")

    # Print statistics
    print(f"Unzipped folder created in: {target_directory}")
    if exclude_string is not None:
        print(f"Files removed with name containing string: {exclude_string}\n")
    print(f"Total zip files: {total_zip_files}")
    print(f"Successfully unzipped: {successful_unzips}")
    print(f"Failed to unzip: {total_zip_files - successful_unzips}")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="JPLAG plagiarism checker")
    parser.add_argument('-e','--exclude-file-with-string', dest='exclude_file', help="Exclude files with name containing string", default=None)
    parser.add_argument('root_folder_path', type=str,help='Root path to zipped submissions folder')
    parser.add_argument('target_directory_path', type=str,help='Path to create new directory to save unzipped files')

    args = parser.parse_args()
 
    main(args.root_folder_path,args.target_directory_path,args.exclude_file)