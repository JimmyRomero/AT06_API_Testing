from Python.Practices.Practice1.Age_converter import age_in_minutes
from Python.Practices.Practice1.Age_converter import age_in_hours
from Python.Practices.Practice1.Age_converter import age_in_days
from Python.Practices.Practice1.Print_messages import print_messages

dict = {}


def users_dictionary():
    global dict
    dictionary_length = int(input("Insert the amount of users: "))
    for i in range(1, dictionary_length + 1):
        key_name = input("Insert the name: ")
        value_age = int(input("Insert the age: "))
        dict[key_name] = value_age
    return dict


def dictionary_ages_in_minutes(dictionary):
    list_ages_in_minutes = []
    list_ages = list(dictionary.values())
    for i in range(0, len(list_ages)):
        list_ages_in_minutes.append(age_in_minutes(list_ages[i]))
    print(list_ages_in_minutes)


def dictionary_ages_in_hours(dictionary):
    list_ages_in_hours = []
    list_ages = list(dictionary.values())
    for i in range(0, len(list_ages)):
        list_ages_in_hours.append(age_in_hours(list_ages[i]))
    print(list_ages_in_hours)


def dictionary_ages_in_days(dictionary):
    list_ages_in_days = []
    list_ages = list(dictionary.values())
    for i in range(0, len(list_ages)):
        list_ages_in_days.append(age_in_days(list_ages[i]))
    print(list_ages_in_days)


def dictionary_messages(dictionary):
    list_for_messages = []
    list_ages = list(dictionary.values())
    for i in range(0, len(list_ages)):
        list_for_messages.append(print_messages(list_ages[i]))
    print(list_for_messages)


users_dictionary()
dictionary_ages_in_minutes(dict)
dictionary_ages_in_hours(dict)
dictionary_ages_in_days(dict)
dictionary_messages(dict)
