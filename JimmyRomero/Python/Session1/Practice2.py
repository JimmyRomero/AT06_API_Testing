def perform_operation(operator, number1, number2):
    global res
    if operator == "+":
        res = number1 + number2
    if operator == "-":
        res = number1 - number2
    if operator == "*":
        res = number1 * number2
    if operator == "/":
        res = number1 / number2
    print(res)


perform_operation("+", 10, 20)
perform_operation("-", 10, 20)
perform_operation("*", 10, 20)
perform_operation("/", 10, 20)
