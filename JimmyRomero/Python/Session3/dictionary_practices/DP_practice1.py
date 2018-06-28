dict = {}


def ask_and_fill_dictionaty():
    global dict
    dictionary_length = int(input("Insert the length of the dictionary: "))
    for i in range(1, dictionary_length + 1):
        key = input("Insert the key: ")
        value = input("Insert the value: ")
        dict[key] = value
    return dict


def print_dictionary_keys(dictionary):
    print(dictionary.keys())


def print_dictionary_values(dictionary):
    print(dictionary.values())


def print_dictionary(dictionary):
    print(dictionary)


def is_key_in_dictionary(dictionary):
    text = input("Insert KEY to know if exists in the dictionary: ")
    if text in dictionary.keys():
        print("The KEY exists!")
    else:
        print("The KEY does not exist!")


def is_value_in_dictionary(dictionary):
    text = input("Insert VALUE to know if exists in the dictionary: ")
    if text in dictionary.values():
        print("The VALUE exists!")
    else:
        print("The VALUE does not exist!")


ask_and_fill_dictionaty()
print_dictionary_keys(dict)
print_dictionary_values(dict)
print_dictionary(dict)
is_key_in_dictionary(dict)
is_value_in_dictionary(dict)
