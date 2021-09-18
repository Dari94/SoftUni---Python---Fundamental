from _collections import defaultdict

resources = defaultdict(int)

while True:
    resource = input()
    if resource == "stop":
        break
    quantity = input()
    resources[resource] += int(quantity)

for (resource, quantity) in resources.items():
    print(f'{resource} -> {quantity}')

