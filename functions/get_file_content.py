import os

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    target_dir = abs_working_directory
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(target_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(target_file, "r") as f:
            content = f.read(MAX_CHARS)
            if len(content) == MAX_CHARS:
                content += f'[...File "{file_path}" truncated at 10000 characters]'
            return content
    except Exception as e:
        return f"Error reading file {file_path}: {e}"
