import os

def write_file(working_directory: str, file_path: str, content: str) -> str:

    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_file_path = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs

        if not valid_file_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'   

        if os.path.isdir(file_path):
            f'Error: Cannot write to "{file_path}" as it is a directory'

        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        f'Error: Cannot write to "{file_path}" as it is a directory'

        with open(f"{target_path}", "r", encoding="utf-8") as file:
            content = file.read(READ_LIMIT)
            if file.read(1):
                content += f'[...File "{file_path}" truncated at {READ_LIMIT} characters]'
            return content