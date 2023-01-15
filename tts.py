#!/usr/bin/env python
from gtts import gTTS
import os
from readfile import extract_words_from_files, read_file_path_from_command_line
# CONSTANTS
AUDIO_PATH = "./audio" 

# os.system("start adjective.mp3")

def generate_audio_file_name(word):
    return word.lower().replace(" ", "_")

def generate_speech_from_text(text):
    audio_file_name = generate_audio_file_name(text)
    audio = gTTS(text=text, lang="en", slow=False)
    audio.save(f"{AUDIO_PATH}/{audio_file_name}.mp3")

if __name__ == "__main__":
    file_path, error = read_file_path_from_command_line()
    if error:
        print(error)
    else:
        words = extract_words_from_files(file_path)
        for w in words:
            generate_speech_from_text(w)  