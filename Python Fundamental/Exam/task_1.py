
#lists exam - april 2020
string = input()
command = input()

while command != 'Done':
    arg = command.split(' ')
    current_command = arg[0]
    if current_command == 'TakeOdd':
        string = string[1::2]
        print(string)
    elif current_command == 'Cut':

        index = int(arg[1])
        length = int(arg[2])

        if index in range(len(string)) and (index + length) in range(len(string)+1):
            substring = string[index: index + length]
            string = string.replace(substring, "",1)
            print(string)
    elif current_command == 'Substitute':
        substring = arg[1]
        substitute = arg[2]
        if substring in string:
            string = string.replace(substring,substitute)
            print(string)
        else:
            print("Nothing to replace!")
    command = input()

print(f"Your password is: {string}")

