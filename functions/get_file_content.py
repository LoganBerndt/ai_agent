import os
from config import READ_LIMIT


def get_file_content(working_directory: str, file_path: str) -> str:

    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_file_path = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs

        if not valid_file_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'    

        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(f"{target_path}", "r", encoding="utf-8") as file:
            content = file.read(READ_LIMIT)
            if file.read(1):
                content += f'[...File "{file_path}" truncated at {READ_LIMIT} characters]'
            return content



    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    get_file_content(working_directory, file_path)