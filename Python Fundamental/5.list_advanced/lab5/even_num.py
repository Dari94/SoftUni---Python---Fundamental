string = input().split(", ")
numbers = [int(n.strip()) for n in string]
even_number_indexes = []

for index, numbers in enumerate(numbers):
    if numbers % 2 == 0:
        even_number_indexes.append(index)
print(even_number_indexes)