#!/usr/bin/env python
import sys
import json

def extract_word_list_from_json_files(file_path):
    f = open(file_path, "rt")
    # array of word
    # word: word, phoneticRespelling,definition[],example[],synonym[]    
    return json.loads(f.read())

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


def get_file_name(file_path):
    file_path_components = file_path.split('/')
    file_name_and_extension = file_path_components[-1].rsplit('.', 1)
    return file_name_and_extension[0]

def read_file_content(file_path):
    content = ""
    try:        
        # opens file for reading in text mode
        file_handler = open(file_path, "rt")
        # read lines
        while True:
            line = file_handler.readline()
            if len(line):
                content = content + "{}".format(line)
            if not line:
                break
        # close
        file_handler.close()
    except Exception as e:
        print(e)
    return content

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
        words = extract_word_list_from_json_files(file_path)
        # words = extract_words_from_files(file_path)
        for w in words:
            print("{}".format(w))    