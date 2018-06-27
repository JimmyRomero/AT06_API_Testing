def area_of_circle(radius):
    pi = 3.1416
    if radius > 10:
        area = pi * (radius * 2)
        print(area)
    else:
        print("Invalid radius: less than 10")


area_of_circle(15)
area_of_circle(10)
area_of_circle(20)


def sum_to(number):
    accumulator = 0
    for i in range(number + 1):
        if i <= 35:
            accumulator += i
    print(accumulator)


sum_to(10)
sum_to(35)
sum_to(40)
