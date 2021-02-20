from page_loader.errors import SomethingWrongError


def save(content, path_to_file, mode='w'):
    try:
        with open(path_to_file, mode) as file:
            file.write(content)
    except OSError as er:
        raise SomethingWrongError(f'{er}') from er
