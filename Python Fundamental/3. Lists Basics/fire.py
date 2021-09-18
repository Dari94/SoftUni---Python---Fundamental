fires = input().split("#")
water = int(input())
result = []
effort = 0
total_fire = 0
for fire in fires:
    valid = None
    fire_level = fire.split(" = ")
    if fire_level[0] == "High" and int(fire_level[1]) in range (81,126):
        valid = True
    elif fire_level[0] == "Medium" and int(fire_level[1]) in range (51,81):
        valid = True
    elif fire_level[0] == "Low" and int(fire_level[1]) in range(1, 51):
        valid = True

    if water - (int(fire_level[1])) >= 0 and valid is True:
        water -= (int(fire_level[1]))
        effort += (int(fire_level[1])*0.25)
        total_fire +=(int(fire_level[1]))
        result.append(int(fire_level[1]))
print(f'Cells:')
for cell in result:
    print(f' - {cell}')
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")

