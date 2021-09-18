num_wagons = int(input())
train= [0] * num_wagons

while True:
    command = input()
    if command == 'End':
        break

    tokens =command.split(' ')
    instructions = tokens[0]

    if instructions == 'add':
        train[-1] += int(tokens[1])
    elif instructions == 'insert':
        index = int(tokens[1])
        count = int(tokens[2])
        train[index] += count
    elif instructions == 'leave':
        index = int(tokens[1])
        count = int(tokens[2])
        train[index] -= count



print(train)