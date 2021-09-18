product_price_dict = {}

while True:
    command = input()
    if command == "buy":
        break

    product, price, quantity = command.split(" ")
    if product in product_price_dict:
        product_price_dict[product][0] = float(price)
        product_price_dict[product][1] += int(quantity)
    else:
        product_price_dict[product] = [float(price), float(quantity)]
for key, value in product_price_dict.items():
        print(f"{key} -> {value[0] * value[1] :.2f}")
