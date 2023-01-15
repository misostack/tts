#!/usr/bin/env python
import sys

def extract_words_from_files(file_path):
    words = []
    try:        
        # opens file for reading in text mode
        file_handler = open(file_path, "rt")
        # read lines
        while True:
            line = file_handler.readline()
            if len(line):
                words.append(line.strip())
            if not line:
                break
        # close
        file_handler.close()
    except Exception as e:
        print(e)
    return words

def read_file_path_from_command_line():
    file_path, error = "", None
    try:
        if len(sys.argv) < 2:
            raise Exception("Error: Please specify file path")    
        # read file name from command line arguments
        file_path = sys.argv[1]
    finally:
        return file_path, error

if __name__  == "__main__":
    file_path, error = read_file_path_from_command_line()
    if error:
        print(error)
    else:
        words = extract_words_from_files(file_path)
        for w in words:
            print("{}".format(w))    