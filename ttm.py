#!/usr/bin/env python
from gtts import gTTS
from readfile import extract_words_from_files, read_file_path_from_command_line, get_file_name
from markdowngen import generate_markdown_for_words

if __name__ == "__main__":
    file_path, error = read_file_path_from_command_line()
    if error:
        print(error)
    else:
        words = extract_words_from_files(file_path)
        file_name = get_file_name(file_path)
        generate_markdown_for_words(file_name, words)