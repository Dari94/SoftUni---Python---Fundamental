def validate_containing_value(my_dict, key, def_value = 0):
    if key not in my_dict:
        my_dict[key] = def_value


force_book = {}

while True:
    command = input()

    if command == "Lumpawaroo":
        break
    side = ""
    user = ""

    if " | " in command:
        args = command.split(" | ")
        side = args[0]
        user = args[1]

        all_users = [item for current_list in force_book.values() for item in current_list ]

        if user not in all_users:
            validate_containing_value(force_book, side, [])
            force_book[side].append(user)

    else:
        args = command.split(" -> ")
        user = args[0]
        side = args[1]
        side_of_users = ""
        for k,v in force_book.items():
            if user in v:
                side_of_users = k
                break

        if side_of_users != "":
            force_book[side_of_users].remove(user)

        validate_containing_value(force_book, side, [])
        force_book[side].append(user)
        print(f"{user} joins the {side} side!")

force_book_sorted = dict(sorted(force_book.items(), key = lambda x:(-len(x[1]), x[0])))

for (k, v) in force_book_sorted.items():
    if len(v) > 0:
        print(f"Side: {k}, Members: {len(v)}")
        value_sorted = sorted(v)
        for s in value_sorted:
            print(f"! {s}")