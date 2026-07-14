import os

def get_files_info(working_directory: str, directory: str = ".") -> str:

    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if valid_target_dir:
            if os.path.isdir(target_dir):
                all_items:list = []
                for item in os.listdir(target_dir):
                    item_path = os.path.join(target_dir, item)
                    all_items.append(f"- {item}: file_size={os.path.getsize(item_path)}, is_dir={os.path.isdir(item_path)}") 
                    
                all_items = "\n".join(all_items)
                return all_items
                return f'Success: "{directory}" is within the working directory'
            else:
                return f'Error: "{directory}" is not a directory'
        else:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'    
    except Exception as e:
        return f"Error: {e}"


schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
