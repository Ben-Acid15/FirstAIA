import os
import functions.config


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: "File not found or is not a regular file: "{file_path}"'
    file_content = ""
    file_content_list = []
    try:
        with open(target_file, 'r') as file:
            file_content = file.read()
        if len(file_content.split()) > 10000:
            file_content = file_content[:10000] + "\n[...File '{file_path}' truncated at 10000 characters]"
    except Exception as e:
        return f"Error: Error while reading file: {e}"
    return file_content
        
    