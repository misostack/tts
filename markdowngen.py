#!/usr/bin/env python
from jinja2 import Template
from writefile import write_file, generate_image_for_word
from readfile import read_file_content, get_file_name, extract_word_list_from_json_files
from tts import generate_slug_for_word, generate_speech_from_text, generate_script_from_word


def generate_markdown_for_word(word):
    content = read_file_content("./template/word.md")
    template = Template(content)
    data = {
        "word": word
    }
    markdown_dir = './markdown'
    file_name = generate_slug_for_word(word)
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

def build_word_script(w):
    word_script = ""
    word_script += w["word"] + "\n"    

    word_script += "Definitions" + "\n"
    for definition in w["definitions"]:
        word_script += definition + "\n"

    word_script += "Examples" + "\n"
    for example in w["examples"]:
        word_script += example + "\n"

    word_script += "Synonyms" + "\n"
    for synonym in w["synonyms"]:
        word_script += synonym + "\n"        
    return word_script

def generate_rich_markdown_content_for_words(file_name, words):
    try:
        content = read_file_content("./template/rich-word.md")
        template = Template(content)
        markdown_dir = './markdown'
        number_of_word = 0
        for w in words:        
            append = True
            if number_of_word == 0:
                append = False
            number_of_word += 1
            word_slug = generate_slug_for_word(w['word'])
            data = {
                "index": number_of_word,
                "word": w['word'].capitalize(),
                "phonetic_respelling": w["phonetic_respelling"],
                "definitions": w["definitions"],
                "examples": w["examples"],
                "synonyms": w["synonyms"],
                "word_script": f"{word_slug}_script"
            }
            generate_speech_from_text(w['word'])  
            generate_script_from_word(w['word'],build_word_script(w))
            generate_image_for_word(w['word'], f"./images/{word_slug}.png")
            write_file(f"{markdown_dir}/{file_name}.md", template.render(data), append)            
    except Exception as e:
        print(e)

if __name__ == "__main__":
    file_path="./words/grammar_keys.json"
    words = extract_word_list_from_json_files(file_path)
    file_name = get_file_name(file_path)
    generate_rich_markdown_content_for_words(file_name, words)