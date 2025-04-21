import pandas


def read_console():
    """
    Read the console input
    :return:
    """
    return input("Enter your input: ")

def read_file(path):
    """
    Read file from path
    :param path: path to the file to be read
    :return:
    """
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

def read_file_pandas(path):
    """
    Read file from path using pandas module
    :param path: path to the file to be read
    :return:
    """
    text = pandas.read_csv(path)
    return text.to_string()