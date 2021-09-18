lost_fights = int(input())

expenses = 0.00
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

for fight_count in range(1, lost_fights+1):

    if fight_count % 2 == 0:
        expenses += helmet_price

    if fight_count % 3 == 0:
        expenses += sword_price

    if fight_count % 2 == 0 and fight_count % 3 == 0:
        expenses += shield_price

    if fight_count % 4 == 0 and fight_count % 6 == 0:
        expenses += armor_price

print(f'Gladiator expenses: {expenses:.2f} aureus')