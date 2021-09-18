string = input()
new_string = "".join([chr(ord(ch)+3) for ch in string])
print(new_string)