def print_messages(age):
    if age <= 12:
        return "You are a child"
    if 13 <= age <= 17:
        return "You are teenager"
    if 17 <= age <= 29:
        return "You are young"
    if age >= 30:
        return "You are a adult"
