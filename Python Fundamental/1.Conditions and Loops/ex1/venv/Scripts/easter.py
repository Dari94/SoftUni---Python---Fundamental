budget = float(input())
floor_price = float(input())

egg_price = 0.75 * floor_price
milk_litter_price = 1.25 * floor_price
milk_price = milk_litter_price / 4

cozonac_price = egg_price + milk_price + floor_price
colored_eggs_count = 0
cozonac_count = 0

while budget >= cozonac_price:
    cozonac_count += 1
    colored_eggs_count += 3

    if cozonac_count % 3 == 0:
        colored_eggs_count -= cozonac_count - 2

    budget -= cozonac_price
print(f'You made {cozonac_count} cozonacs! Now you have {colored_eggs_count} eggs and {budget:.2f}BGN left.')

