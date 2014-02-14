labic-parse-tweets
==================
This script contains functions to remove duplicate lines from CSV files and
remove the null byte character. It lazily reads all the file at once, so you may 
need a lot of memorym depending on the size of your CSV.

------------------
Purpose:
------------------
This script was created to remove duplicate lines from CSV, pipe delimited files and
remove the null byte character. You can change it to use another delimiter.

------------------
Requirements:
------------------
* Python3.3 or newer

------------------
Usage:
------------------
* Download the files;
* Extract the contents of the downloaded file;
* Put the CSV that you wish to remove duplicates in the same folder as the script;
* In a shell/terminal/windows command prompt run the following command:

python3.3 file_fix.py "file_example.csv"

Notes:
* In this example, the python3.3 install had the binary python3.3.
* The csv input file was named "file_example.csv".

------------------
Results:
------------------
When the script is done running, if the input CSV file was named "file_example.csv", the results will be:
    * file_example_FIXED.csv - a CSV file without the null byte character, but with duplicate lines and pipe delimited;        
    * file_example_FIXED_NO_DUPLICATES.csv - a CSV file, semi colon delimited. Without duplicate tweets and null byte.


------------------
BETA
------------------
This script is in Beta stage, which means it may contain errors or inaccurate results. Feel free(and please do so!) to report any bugs you find. 

