def determine_odd_or_even(number):
    if number % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")


determine_odd_or_even(2)
determine_odd_or_even(3)
determine_odd_or_even(4)


def is_prime_or_not(min, max):
    for number in range(min, max):
        prime = 1
        for i in range(2, (number // 2) + 1):
            if number % i == 0:
                prime = 0
                break
        if prime:
            print(number, " is prime")
        else:
            print(number, " is not prime")


is_prime_or_not(1, 10)
