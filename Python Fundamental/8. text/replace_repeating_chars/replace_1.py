string = input()

for ch in string:
    string = string.replace(ch * 2, ch)

print(string)