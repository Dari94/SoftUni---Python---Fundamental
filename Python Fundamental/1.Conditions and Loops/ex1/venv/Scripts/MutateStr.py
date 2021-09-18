string_1 = input()
string_2 = input()
new_str = ""
for i in range(len(string_1)):
    if string_1[i] != string_2[i]:
        new_str = string_2[0: (i + 1)] + string_1[(i + 1):len(string_1)]
        print(new_str)
