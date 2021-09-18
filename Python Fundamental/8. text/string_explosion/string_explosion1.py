string = input()
power = 0
i=0
while i < len(string):
    ch = string[i]
    if ch == ">":
        power += int(string[i+1])
    elif power >0:
        string = string[:i] + string[i +1:]
        i -= 1
        power -= 1

    i += 1
print(string)