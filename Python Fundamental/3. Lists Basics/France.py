collection = input().split("|")
budget = float(input())
result = []
profit = 0
revenue = 0
for item in collection:
    valid = None
    item_type = item.split("->")
    if item_type[0] == "Clothes" and float(item_type[1]) <= 50.00:
        valid = True

    elif item_type[0] == "Shoes" and float(item_type[1]) <= 35.00:
        valid = True

    elif item_type[0] == "Accessories" and float(item_type[1]) <= 25.50:
        valid = True

    if valid is True and budget - float(item_type[1]) >= 0:
            budget -= float(item_type[1])
            result.append(float(item_type[1])*1.40)
            revenue += float(item_type[1])*1.40
            profit += float(item_type[1])*1.40 - float(item_type[1])
budget += profit + revenue
for tag in result:
    print(f"{tag:.2f}", end=" ")
print(f"\nProfit: {profit:.2f}")
if budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")