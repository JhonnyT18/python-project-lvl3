def write_to_file(content, path_to_file, mode='w'):
    try:
        with open(path_to_file, mode) as file:
            file.write(content)
    except OSError:
        raise
