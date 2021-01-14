def write_to_file(content, path_to_file, mode='w'):
    with open(path_to_file, mode) as file:
        file.write(content)
