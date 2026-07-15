import os
import subprocess

# run_python_file.py - This function executes a specified Python file within a given working directory. 
def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:

    result_output: list[str] = []

    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_file_path = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs

        if not valid_file_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not target_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        run_command = ["python", target_path]

        if args is not None:
            run_command.extend(args)

        result = subprocess.run(
            run_command,
            timeout=30,
            cwd=working_dir_abs,
            capture_output=True,
            text=True,
        )

        stdout_clean = result.stdout.strip() if result.stdout else ""
        stderr_clean = result.stderr.strip() if result.stderr else ""

        if not result.returncode == 0:
            result_output.append(f"Process exited with code {result.returncode}") 

        if not stdout_clean and not stderr_clean:
            result_output.append("No output produced")
        
        if stdout_clean:
            result_output.append(f"STDOUT: {result.stdout.strip()}")

        if stderr_clean:
            result_output.append(f"STDERR: {result.stderr.strip()}")

        return "\n".join(result_output)
        
        

    except subprocess.CalledProcessError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a Python file in the specified working directory with optional arguments",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python file to execute, relative to the working directory"
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Arguments to pass to the Python file"
                }
            },
            "required": ["file_path"]
        }
    }
}

