def write_console(text):
    """
    Write output to console
    :param text: Text to write
    :return:
    """
    print(text)

def write_file(text, path):
    """
    Write output to file using path
    :param path: path to the file to be written
    :param text: Text to write
    :return:
    """
    try:
        with open(path, 'a', encoding='utf-8') as file:
            file.write(text+ '\n')
    except FileNotFoundError:
        raise FileNotFoundError('File not found')