input_string = input().split("|")
energy = 100
coins = 100
gain_energy = 0
for event in input_string:
    event_type = event.split("-")
    if event_type[0] == "rest":
        gain_energy = int(event_type[1])

        if energy < 100:
            energy += gain_energy
            print(f"You gained {gain_energy} energy.")
            print(f"Current energy: {energy}.")

        else:
            print(f"You gained {0} energy.")
            print(f"Current energy: {100}.")
    elif event_type[0] == "order":
        if energy - 30 >= 0:
            energy -= 30
            coins += int(event_type[1])
            print(f"You earned {event_type[1]} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins - int(event_type[1]) > 0:
            coins -= int(event_type[1])
            print(f"You bought {event_type[0]}.")
        else:
            print(f"Closed! Cannot afford {event_type[0]}.")
            exit()


print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")
