def multiply(a, b):
    return a * b



def add(a, b):
    return a + b


def divide(a, b):
    return a // b



def subtract(a, b):
    return a - b


def execute(a, b, operator):
    mapping = [
        ['multiply', multiply],
        ['add', add],
        ['divide', divide],
        ['subtract', subtract],
    ]

    for operator_name , fn in mapping:
        if operator_name == operator:
            return fn(a,b)


input_operator = input()
num_1 = int(input())
num_2 = int(input())
print(execute(num_1, num_2, input_operator))