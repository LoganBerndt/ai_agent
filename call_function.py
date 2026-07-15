import json
from functions.get_files_info import get_files_info, schema_get_files_info
from functions.get_file_content import get_file_content, schema_get_file_content
from functions.run_python_file import run_python_file, schema_run_python_file
from functions.write_file import write_file, schema_write_file
from collections.abc import Callable

# The call function is responsible for executing the function calls made by the AI agent. It takes in a tool_call object, which contains the name 
# of the function to be called and its arguments. The function then maps the function name to the corresponding function and executes it with the 
# provided arguments. The result is returned in a structured format, including the role, tool_call_id, and content of the result.

available_functions = [
    schema_get_files_info,
    schema_get_file_content,
    schema_run_python_file,
    schema_write_file   
]

def call_function(tool_call, verbose:bool = False) -> dict:
    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments or "{}")

    if verbose:
        print(f" - Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")

    function_map: dict[str, Callable[..., str]] = {
    "get_file_content": get_file_content,
    "get_files_info": get_files_info,
    "run_python_file": run_python_file,
    "write_file": write_file
    }

    if function_name not in function_map:
        return {
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": f"Error: Unknown function: {function_name}",
        }
    else:
        function_args["working_directory"] = "./calculator"
        result = function_map[function_name](**function_args)

        return {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": result,
        }