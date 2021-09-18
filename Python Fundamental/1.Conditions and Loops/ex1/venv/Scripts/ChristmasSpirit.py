quantity = int(input())
days = int(input())


spirit_count = 0
total_cost = 0
days_count = 1
while days >= days_count:
    if days_count % 11 == 0:
        quantity += 2

    if days_count % 2 == 0:
        total_cost += quantity * 2
        spirit_count += 5

    if days_count % 3 == 0:
        total_cost += quantity * 5 + quantity * 3
        spirit_count += 13

    if days_count % 5 == 0:
        total_cost += quantity * 15
        spirit_count += 17

    if days_count % 3 == 0 and days_count % 5 == 0:
        spirit_count += 30

    if days_count % 10 == 0:
        spirit_count -= 20
        total_cost += 23

    days_count += 1
if days % 10 == 0:
    spirit_count -= 30

print(f'Total cost: {total_cost}')
print(f'Total spirit: {spirit_count}')
