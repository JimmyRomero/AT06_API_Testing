def ask_and_fill_array():
    value = int(input("Insert the number of elements to insert in the list: "))
    list = []
    for i in range(1, value + 1):
        list_value = input("Insert value: ")
        list.append(list_value)
    return list


def print_the_array(array):
    print(array)


print_the_array(ask_and_fill_array())
