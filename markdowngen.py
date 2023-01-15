#!/usr/bin/env python
from jinja2 import Template
from writefile import write_file
from readfile import read_file_content
from tts import generate_audio_file_name


def generate_markdown_for_word(word):
    content = read_file_content("./template/word.md")
    template = Template(content)
    data = {
        "word": word
    }
    markdown_dir = './markdown'
    file_name = generate_audio_file_name(word)
    write_file(f"{markdown_dir}/{file_name}.md", template.render(data))

def generate_markdown_for_words(file_name, words):
    content = read_file_content("./template/word.md")
    template = Template(content)
    markdown_dir = './markdown'
    number_of_word = 0
    for w in words:        
        append = True
        if number_of_word == 0:
            append = False
        number_of_word += 1
        data = {
            "index": number_of_word,
            "word": w.capitalize()
        }        
        write_file(f"{markdown_dir}/{file_name}.md", template.render(data), append)    
        


if __name__ == "__main__":
    generate_markdown_for_words("words", ["test", "abc"])