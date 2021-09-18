lines = int(input())
sum_quantity = 0
capacity = 255


for i in range(0, lines, 1):
    quantity = int(input())

    if sum_quantity + quantity > capacity:
        print(f'Insufficient capacity!')
    else:
        sum_quantity += quantity

print(sum_quantity)