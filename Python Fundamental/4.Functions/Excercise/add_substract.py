def sum_numbers(num_one, num_two):
    return num_one + num_two


def subtract(first_num, second_num):
    return first_num - second_num


def add_and_subtract(num_one,num_two, num_three):
    sum_one = sum_numbers(num_one,num_two)
    res = subtract(sum_one, num_three)
    print(res)


a = int(input())
b = int(input())
c= int(input())
add_and_subtract(a, b, c)
