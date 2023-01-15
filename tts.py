#!/usr/bin/env python
from gtts import gTTS
import os
from readfile import extract_words_from_files, read_file_path_from_command_line, read_file_content
# CONSTANTS
AUDIO_PATH = "./audio" 

# os.system("start adjective.mp3")

def generate_audio_file_name(word):
    return word.lower().replace(" ", "_")

def generate_speech_from_text(text):
    audio_file_name = generate_audio_file_name(text)
    audio_file_path = f"{AUDIO_PATH}/{audio_file_name}.mp3"
    if not os.path.exists(audio_file_path):    
        audio = gTTS(text=text, lang="en", slow=False)
        audio.save(audio_file_path)

def generate_example_from_word(word):
    word_example = f"{generate_audio_file_name(word)}_example"
    file_path = f"./words/{word_example}.txt"
    if os.path.exists(file_path):
        audio_file_path = f"{AUDIO_PATH}/{word_example}.mp3"
        if not os.path.exists(audio_file_path):
            content = read_file_content(file_path)
            audio = gTTS(text=content, lang="en", slow=False)
            audio.save(audio_file_path)


if __name__ == "__main__":
    file_path, error = read_file_path_from_command_line()
    if error:
        print(error)
    else:
        words = extract_words_from_files(file_path)
        for w in words:
            generate_speech_from_text(w)  
            generate_example_from_word(w)