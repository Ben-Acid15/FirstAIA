import os
from config.py import file_char_limit

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(file_path):
        return f'Error: "File not found or is not a regular file: "{file_path}"'
    file_content = ""
    try:
        with open(target_file, 'r') as file:
            file_content = file.read()
        if len(file_content.list()) > 10000:
            count = 0
            for char in file_content.list():
                while count <= 10000:
                    file_content_list.append(char)
                    count += 1
            file_content = file_content_list.join() + "\n[...File '{file_path}' truncated at 10000 characters]"
    except Expection as e:
        return "Error: Error while reading file: {e}"
        
    