number = int(input())
packing_dictionary = {}
username = None
license_plate_num = None

for _ in range(number):

    data = input().split(" ")
    if data[0] == "register":
        username = data[1]
        license_plate_num = data[2]
        if username not in packing_dictionary:
            packing_dictionary[username] = license_plate_num
            print(f"{username} registered {license_plate_num} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_num}")
    elif data[0] == "unregister":
        username = data[1]
        if username not in packing_dictionary:
            print(f"ERROR: user {username} not found")
        else:
            packing_dictionary.pop(username)
            print(f"{username} unregistered successfully")

for (key,value) in packing_dictionary.items():
    print(f"{key} => {value}")