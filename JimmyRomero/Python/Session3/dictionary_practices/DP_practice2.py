dict = {}


def fill_dictionaty():
    global dict
    key = int(input("Insert the key: "))
    if 1 <= key <= 9:
        dict[key] = key * key
    while 1 <= key <= 9:
        key = int(input("Insert the key: "))
        if 1 <= key <= 9:
            dict[key] = key * key
        else:
            break
    print(dict)
    return dict


fill_dictionaty()


def prime_dictionary(dictionary):
    prime_dict = {}
    for number in range(1, len(dictionary)):
        prime = 1
        for i in range(2, (number // 2) + 1):
            if dictionary[number] % i == 0:
                prime = 0
                break
        if prime:
            prime_dict[number] = dictionary.get(number)

    print(prime_dict)


prime_dictionary(dict)
