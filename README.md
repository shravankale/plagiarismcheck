Contains scripts for checking plagiarism across a set of files. It uses the JPLAG (https://github.com/jplag/JPlag) plagiarism checker. 

#### Pre-requirement 
1. Requires JDK 17
2. Fetch the jplag-X.Y.Z-jar-with-dependencies.jar from [https://github.com/jplag/JPlag](https://github.com/jplag/jplag/releases)

#### How to check for plagiarism
1. Use the unzip-script.py to unzip a directory full of zips.
    - Usage: python unzip_script.py [root_folder_path] [target_directory_path]
    - root_folder_path = Source of the directory containing the zips (Example: submissions)
    - target_directory_path =  Source of the directory to store unzipped files in sub-directories (Example: submissions-unzip)
    - The sub-directory in the target directory is named after the zip file.
2. Use the jplag.sh to run the plagiarism checker
    - Convert the jplag.sh to an executable using ```chmod u+x jplag.sh```(MacOS/Linux).
    - The jplag.sh contains some default values that may need to be changed
    - Comments are added to describe the option flags and values used. Additional options can be found on https://github.com/jplag/JPlag.
    - Run the script using ```./jplag.sh [path_to_jar] [path_to_unzipped_submissions]```
    - path_to_jar = Path to the dowloaded jplag-X.Y.Z-jar-with-dependencies.jar
    - path_to_unzipped_submissions = Path to unzipped submissions from Step 1 (Example: submissions-unzip)
    - The output of this script will result in the creation of a zip file which will have the name provided by the ```-r``` option flag in jplag.sh (Default: jplag_visualize.zip)
3. Visualization of results:
    - Open the visualizer at [JPLAG visualizer](https://jplag.github.io/JPlag/)
    - Drag and drop the zip (default: jplag_visualize.zip) created in Step 2

Note: If there are any compiler related issues with using the jar file, it may be due to XCode related service agreements that need to be approved.


