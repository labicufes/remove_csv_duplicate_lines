#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
This script was created to remove duplicate lines from CSV, pipe delimited files and
remove the null byte character. You can change it to use another delimi

* Requires:
    Python3.3 or newer.
---------------
USAGE:
---------------
    If your python binary is named python3.3:
    python3.3 file_fix.py "myfile.csv"

See the README.md for more info.
"""
import csv
import os
import sys

DEFAULT_INPUT_DELIMITER = '|'
DEFAULT_OUTPUT_DELIMITER = ';'

def filename_append(str_filename, str_text_to_append):
    """ This function appends a string to the end of a given filename """
    str_filename, str_file_extension = os.path.splitext(str_filename)
    new_filename = str_filename + str_text_to_append + str_file_extension
    return new_filename

def remove_null_byte(str_input_filename='tweets.csv'):
    # rb: the B is for byte
    file_input = open(str_input_filename,"rb")

    # Read the whole CSV at once.
    str_whole_csv = file_input.read()
    file_input.close()

    # Replace the null byte with the empty string.
    str_whole_csv = str_whole_csv.replace(b'\x00', bytes('', 'utf-8'))

    # Writes the resulting file
    str_fixed_filename = filename_append(str_input_filename, '_FIXED')
    file_output = open(str_fixed_filename, 'wb')
    file_output.write(str_whole_csv)
    file_output.close()

def remove_duplicate_lines(str_input_filename='tweets_FIXED.csv'):
    """ 
    This function removes all duplicate lines in a given CSV.
    A line is considered duplicate if another one with the exact 
    same column values exist.
    """

    # Empty set to store all the lines. Sets doesn't keep two copies of the 
    # same object duplicate objects. If an already existing object is trying 
    # to be inserted nothing will happen.
    set_tuple_valid_lines = set()

    with open(str_input_filename, 'rt', encoding="utf8") as csvfile:
        csv_in = csv.reader(csvfile, delimiter=DEFAULT_INPUT_DELIMITER, quoting=csv.QUOTE_NONE)
        # Saving the first line, because sets aren't ordered.
        list_str_first_line = next(csv_in) 

        # Adding all the lines in the set.
        for line in csv_in:
            if len(line) is 13:
                set_tuple_valid_lines.add(tuple(line))

    str_fixed_filename = filename_append(str_input_filename, '_NO_DUPLICATES')
    # Writing all the exclusive lines
    with open(str_fixed_filename, 'w', newline='', encoding="utf8") as csvfile:
        file_writer = csv.writer(csvfile, delimiter=DEFAULT_OUTPUT_DELIMITER, quotechar='"')
        file_writer.writerow(list_str_first_line)
        for line in set_tuple_valid_lines:
            file_writer.writerow(line)

def file_fix(str_input_filename):
    """ This function removes null_byte and duplicate tweets. """
    remove_null_byte(str_input_filename)
    str_temp_filename = filename_append(str_input_filename, '_FIXED')
    remove_duplicate_lines(str_temp_filename)

if __name__ == '__main__':
    str_input_filename = sys.argv[1]
    file_fix(str_input_filename)



