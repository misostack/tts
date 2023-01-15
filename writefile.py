#!/usr/bin/env python
from PIL import Image, ImageDraw, ImageFont

def write_file(file_path, content, append=False):
    error = None
    try:        
        # opens file for reading in text mode
        mode = "wt"
        if append:
            mode = "at"
        file_handler = open(file_path, mode)
        # read lines
        if append:
            file_handler.write(f"\n\n{content}")
        else:
            file_handler.write(content)
        # close
        file_handler.close()
    except Exception as e:
        error = e    
    return error



def generate_image_for_word(message, file_path):
    error = None
    try:     
        width = 940
        height = 788
        font = ImageFont.truetype("arial.ttf", size=80)
        img = Image.open('./word-frame.png')
        imgDraw = ImageDraw.Draw(img)
        _, _, textWidth, textHeight = imgDraw.textbbox((0, 0), message, font=font)
        xText = (width - textWidth) / 2
        yText = (height - 120 - textHeight) / 2
        imgDraw.text((xText, yText), message, font=font, fill=(255, 22, 22))
        img.save(file_path)
    except Exception as e:
        error = e    
    return error    

if __name__  == "__main__":
    error = generate_image_for_word("adjective", "./images/adjective.png")
    if error:
        print(error)
    else:
        print("Generate image successfully!")    
    # error = write_file("./tmp/example.md", "# Example")
    # if error:
    #     print(error)
    # else:
    #     print("Write file successfully!")