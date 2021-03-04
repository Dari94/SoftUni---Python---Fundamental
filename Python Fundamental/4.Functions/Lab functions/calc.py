input_operator = input()
num_1 = int(input())
num_2 = int(input())


def execute(a, b, operator):
    if operator == 'multiply':
        return a * b
    elif operator == 'divide':
        return int(a / b)
    elif operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a - b


print(execute(num_1, num_2, input_operator))
