from _collections import defaultdict
occurrences = defaultdict(int)
string = input()
chars = [ch for ch in string if ch != " "]
for char in chars:
    occurrences[char] += 1
for char,num in occurrences.items():
    print(f'{char} -> {num}')
