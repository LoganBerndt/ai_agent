from functions.get_file_content import get_file_content


result = get_file_content("calculator", "lorem.txt")
print(result[-200:])
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")

def test_get_files(filename, file_content):
    print(filename)
    print(file_content)


test_get_files("main.py", get_file_content("calculator", "main.py"))

test_get_files("pkg/calculator.py", get_file_content("calculator", "pkg/calculator.py"))

test_get_files("/bin/cat", get_file_content("calculator", "/bin/cat"))

test_get_files("pkg/does_not_exist.py", get_file_content("calculator", "pkg/does_not_exist.py"))
