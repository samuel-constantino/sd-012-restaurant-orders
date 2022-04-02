from csv import DictReader


def validate_extension(path_to_file):
    path_split = path_to_file.split(".")
    if 'csv' not in path_split:
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")


def reader_csv(path):
    validate_extension(path)
    try:
        with open(path, 'r') as file:
            fieldnames = ['name', 'food', 'day']
            dict_list_csv = DictReader(file, fieldnames=fieldnames)
            return [row for row in dict_list_csv]
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path}'")
