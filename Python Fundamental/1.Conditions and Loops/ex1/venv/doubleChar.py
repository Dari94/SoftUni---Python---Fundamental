word = input()
new_word = ""

for i in range(0, len(word), 1):
    new_word += 2*word[i]
print(new_word)