def table_of_letters():
    text = input("Insert the test to validate: ")
    text = text.lower()
    dict = {}
    for i in range(1, len(text)):
        if not (text[i] == " "):
            dict[text[i]] = text.count(text[i])
    dict = sorted(dict.items())
    print(dict)


table_of_letters()
