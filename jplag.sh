#Option Flags:
#Positional argument 1: Path to the jplag-X.Y.Z-jar-with-dependencies.jar
#positional argument 2: Path to directory with unzipped sub-directories created by unzip-script.py
#-l language
#-t Comparison sensitivity
#-n Maximum number of comparisons shown in the report (-1 for all comparisons)
#-r Name of the output zip for visualizer
#-m Comparison similarity threshold

#Additional options and their associated descriptions can be found at https://github.com/jplag/JPlag#cli

java -jar jplag-4.3.0-jar-with-dependencies.jar ./submissions-p1-unzip2 \
-l python3 \
-t 3 \
-n -1 \
-r submissions-p1-jplags \
-m 0.95