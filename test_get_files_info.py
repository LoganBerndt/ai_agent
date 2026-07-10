from functions.get_files_info import get_files_info


def result_print(dir_name:str, files_info:str) -> str | None:
    if dir_name == ".":
        print("Result for current directory:")
    else:
        print(f"Result for '{dir_name}' directory:")

    if not files_info:
        return ("  - No files found.\n")

    print(files_info)
    

def test_get_files():
    
    result_print(".", get_files_info("calculator", "."))

    result_print("pkg", get_files_info("calculator", "pkg"))

    result_print("/bin", get_files_info("calculator", "/bin"))

    result_print("../", get_files_info("calculator", "../"))



if __name__ == "__main__":
    test_get_files()