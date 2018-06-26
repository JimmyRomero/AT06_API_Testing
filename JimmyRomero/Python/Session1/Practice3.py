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
    if operator == "==":
        res = number1 == number2
    if operator == "!=":
        res = number1 != number2
    if operator == ">":
        res = number1 > number2
    if operator == "<":
        res = number1 < number2
    if operator == ">=":
        res = number1 >= number2
    if operator == "<=":
        res = number1 <= number2
    if operator == "+=":
        res += number1
    if operator == "-=":
        number2 -= number1
    if operator == "*=":
        number2 *= number1
    if operator == "/=":
        number2 /= number1
    if operator == "%=":
        number2 %= number1

    print("number1: ", number1)
    print("number2: ", number2)
    print("Operator: ", operator)
    print("Result:", res)
    print("---------------------------------")
    res = 0


# Arithmetic's operators
perform_operation("+", 10, 20)
perform_operation("-", 10, 20)
perform_operation("*", 10, 20)
perform_operation("/", 10, 20)

# Comparison operators
perform_operation("==", 10, 20)
perform_operation("!=", 10, 20)
perform_operation(">", 10, 20)
perform_operation("<", 10, 20)
perform_operation(">=", 10, 20)
perform_operation("<=", 10, 20)
perform_operation("<=", 10, 20)

# Assignment operators
perform_operation("+=", 10, 20)
perform_operation("-=", 10, 20)
perform_operation("*=", 10, 20)
perform_operation("/=", 10, 20)
perform_operation("%=", 10, 20)

# Membership operators
a = 10
b = 20
listNumbers = [10, 20, 30, 40, 50]

if a in listNumbers:
    print("a exists list")
else:
    print("a does not exist list")

if b not in listNumbers:
    print("b does not exist list")
else:
    print("b exists list")

# Membership operators
value_1 = 15
value_2 = 15

if value_1 is value_2:
    print("Line 1 - a and b have the same identity")
else:
    print("Line 1 - a and b do not have the same identity")

if id(value_1) == id(value_2):
    print("Line 2 - a and b have the same identity")
else:
    print("Line 2 - a and b do not have the same identity")
