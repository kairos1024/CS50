import sys

def code_counter(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            full_lines = [line.strip()
            for line in lines
if line.strip() and not line.strip().startswith('#')]
            return len(full_lines)
    except FileNotFoundError:
        sys.exit("File does not exist.")
    except IOError:
        sys.exit("Error reading the file.")


if len(sys.argv) != 2:
    sys.exit("Usage: python count_lines.py <file.py>")

file_path = sys.argv[1]
if not file_path.endswith('.py'):
    sys.exit("Not a Python file.")

lines_of_code = code_counter(file_path)
print(f"Number of lines of code in {file_path}: {lines_of_code}")
