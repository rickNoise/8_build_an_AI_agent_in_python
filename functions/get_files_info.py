import os

def get_files_info(working_directory, directory=None):

    working_directory_abs = os.path.abspath(working_directory)
    if directory is None:
        directory_abs = working_directory_abs
    elif directory.startswith("/"):
        directory_abs = os.path.abspath(directory)
    else:
        directory_abs = os.path.join(working_directory_abs, directory)
    
    directory_abs = os.path.normpath(directory_abs) # normalise before security check
    if directory_abs and not directory_abs.startswith(working_directory_abs):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(directory_abs):
        return f'Error: "{directory}" is not a directory'

    try:
        # Build and return a string representing the contents of the directory.
        str_rep_of_dir = ""
        for file in os.listdir(directory_abs):
            file_path = os.path.join(directory_abs, file)
            is_dir = "True" if os.path.isdir(file_path) else "False"
            file_size = str(os.path.getsize(file_path))
            file_name = str(file)
            str_rep_of_dir += f"- {file_name}: file_size={file_size} bytes, is_dir={is_dir}\n"
        str_rep_of_dir = str_rep_of_dir.rstrip("\n")
        return str_rep_of_dir
    except Exception as e:
        return f"Error: {str(e)}"
