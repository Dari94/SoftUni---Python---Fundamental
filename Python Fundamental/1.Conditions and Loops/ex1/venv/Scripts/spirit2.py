quantity = int(input())
days = int(input())
cost = 0
christmas_spirit = 0
day_count = 1

while day_count <= days:
    if day_count % 11 == 0:
        quantity += 2

    if day_count % 2 == 0:
        cost += quantity * 2
        christmas_spirit += 5

    if day_count % 3 == 0:
        cost += (quantity * 5) + (quantity * 3)
        christmas_spirit += 13

    if day_count % 5 == 0:
        cost += quantity * 15
        christmas_spirit += 17

    if day_count % 5 == 0 and day_count % 3 == 0:
        christmas_spirit += 30

    if day_count % 10 == 0:
        cost += 23
        christmas_spirit -= 20

    if days % 10 == 0:
        christmas_spirit -= 30

    day_count += 1

print(f"Total cost: {cost}")
print(f"Total spirit: {christmas_spirit}")