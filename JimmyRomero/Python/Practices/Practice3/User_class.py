import re

user_dict = {}


def users_dictionary():
    global user_dict
    dictionary_length = int(input("Insert the length of the dictionary: "))
    for i in range(0, dictionary_length):
        key_user_id = input("Insert the key: ")
        value_user_name = input("Insert the value: ")
        add_user(key_user_id, value_user_name)

    print(user_dict)
    return user_dict


def is_valid_user_id(user_id):
    if re.match("^([0-9]|[1-9][0-9]|100)$", user_id):
        return True
    else:
        return False


def is_valid_user_name(user_name):
    if re.match("^([a-z]{1,8})$", user_name):
        return True
    else:
        return False


def add_user(user_id, user_name):
    if is_valid_user_id(user_id) and is_valid_user_name(user_name):
        user_dict[user_id] = user_name


def amount_of_users_by_id():
    array_coincidences = []
    list_keys = list(user_dict.keys())
    number = input("Insert the number to search: ")
    while int(number) > 10:
        number = input("Insert the number to search: ")
    else:
        for i in range(0, len(list_keys)):
            aux = str(list_keys[i])
            if aux.startswith(number):
                array_coincidences.append(aux)
    print(array_coincidences)


def amount_of_users_by_name():
    array_coincidences = []
    list_values = list(user_dict.values())
    letter = input("Insert the letter value to search: ")
    while letter.__len__() > 1:
        letter = input("Insert the letter value to search: ")
    else:
        for i in range(0, len(list_values)):
            aux = str(list_values[i])
            if aux.startswith(letter):
                array_coincidences.append(aux)
    print(array_coincidences)


def user_group():
    user_key_values = list(user_dict.keys())
    for i in range(0, len(user_key_values)):
        aux = int(user_key_values[i])
        if 1 <= aux <= 25:
            print("User belong Group1")
        if 26 <= aux <= 50:
            print("User belong Group2")
        if 51 <= aux <= 75:
            print("User belong Group3")
        if 76 <= aux <= 100:
            print("User belong Group4")


users_dictionary()
amount_of_users_by_id()
amount_of_users_by_name()
user_group()
