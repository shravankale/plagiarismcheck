#!/bin/bash

#Script Usage
#./jplag.sh [path_to_jar] [path_to_unzipped_submissions]

#Option Flags:
#Positional argument 1: Path to the jplag-X.Y.Z-jar-with-dependencies.jar
#positional argument 2: Path to directory with unzipped sub-directories created by unzip-script.py
#-l language
#-t Comparison sensitivity
#-n Maximum number of comparisons shown in the report (-1 for all comparisons)
#-r Name of the output zip for visualizer
#-m Comparison similarity threshold

#Additional options and their associated descriptions can be found at https://github.com/jplag/JPlag#cli



# Set the paths for the jar file and the directory with unzipped sub-directories
jar_path="$1"
unzipped_dir_path="$2"

# Check if the OS is Windows
if [[ "$OSTYPE" == "msys" ]]; then
    echo "Running on Windows"
    java -jar "$jar_path" "$unzipped_dir_path" ^
    -l python3 ^
    -t 3 ^
    -n -1 ^
    -r jplag_visualize ^
    -m 0.95
# Check if the OS is Linux/Mac
elif [[ "$OSTYPE" == "linux-gnu"* ]] || [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Running on Linux"
    java -jar "$jar_path" submissions-unzip \
    -l python3 \
    -t 3 \
    -n -1 \
    -r jplag_visualize \
    -m 0.90
else
    echo "Unsupported OS"
fi