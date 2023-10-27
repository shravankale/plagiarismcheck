Contains scripts for checking plagiarism across a set of files. It uses the JPLAG (https://github.com/jplag/JPlag) plagiarism checker. 

#### Pre-requirement 
1. Requires JDK 17
2. Fetch the jplag-X.Y.Z-jar-with-dependencies.jar from [https://github.com/jplag/JPlag](https://github.com/jplag/jplag/releases)

#### How to check for plagiarism
1. Use the unzip-script.py to unzip a directory full of zips.
    - Usage: python unzip_script.py [root_folder_path] [target_directory_path]
    - root_folder_path = Source of the directory containing the zips
    - target_directory_path =  Source of the directory to store unzipped files in sub-directories
    - The sub-directory in the target directory is named after the zip file.
2. Use the jplag.sh to run the plagiarism checker
    - Convert the jplag.sh to an executable using ```chmod u+x jplag.sh```.
    - The jplag.sh contains some default values that may need to be changed
    - Comments are added to describe the option flags and values used. Additional options can be found on https://github.com/jplag/JPlag.
    - Run the script using ```./jplag.sh```
    - The output of this script will result in the creation of a zip file which will have the name provided by the ```-r``` option flag in jplag.sh
3. Visualization of results:
    - Open the visualizer at https://github.com/jplag/JPlag#cli
    - Drag and drop the zip created in Step 2c

Note: If there are any compiler related issues with using the jar file, it may be due to XCode related service agreements that need to be approved.


