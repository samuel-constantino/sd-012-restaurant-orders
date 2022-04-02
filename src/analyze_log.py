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


def get_values_list_key(dict_list, key):
    values_list = [item[key] for item in dict_list]
    return set(values_list)


def get_frequency_person(dict_list, key, person):
    dict_frequency = {}
    for item in dict_list:
        if item['name'] == person:
            if item[key] not in dict_frequency:
                dict_frequency[item[key]] = 1
            else:
                dict_frequency[item[key]] += 1
    return dict_frequency


def analyze_log(path_to_file):
    dict_list = reader_csv(path_to_file)

    foods_list = get_values_list_key(dict_list, 'food')
    open_days = get_values_list_key(dict_list, 'day')

    food_frequency_maria = get_frequency_person(dict_list, 'food', 'maria')
    bigger_frequency_maria_food = max(food_frequency_maria.values())
    most_frequent_maria_food = next(
        food[0]
        for food in food_frequency_maria.items()
        if food[1] == bigger_frequency_maria_food
    )

    food_frequency_arnaldo = get_frequency_person(dict_list, 'food', 'arnaldo')
    food_frequency_joao = get_frequency_person(dict_list, 'food', 'joao')
    day_frequency_joao = get_frequency_person(dict_list, 'day', 'joao')

    difference_joao = foods_list.difference(food_frequency_joao)
    days_difference_joao = open_days.difference(day_frequency_joao)

    infos = [
        most_frequent_maria_food,
        str(food_frequency_arnaldo['hamburguer']),
        str(difference_joao),
        str(days_difference_joao)
    ]

    break_line_infos = "\n".join(infos)

    with open('data/mkt_campaign.txt', 'w') as file:
        for item in break_line_infos:
            file.writelines(item)
