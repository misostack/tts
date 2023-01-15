#!/usr/bin/env python
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

if __name__  == "__main__":
    error = write_file("./tmp/example.md", "# Example")
    if error:
        print(error)
    else:
        print("Write file successfully!")