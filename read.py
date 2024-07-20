def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.readlines()
            return [line.strip().split(', ') for line in data]
    except FileNotFoundError:
        print("File not found. Please ensure the file path is correct.")
        return []
