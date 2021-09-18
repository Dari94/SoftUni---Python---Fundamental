def validate_containing_value(my_dict, key, def_value_1 = 0,def_value_2 = 0):
    if key not in my_dict:
        my_dict[key] = def_value

exam_result = {}
while True:
    command = input()

    if command == "exam finished":
        break

    token = command.split("-")
    if len(token) == 3:
        username = token[0]
        language = token[1]
        points = int(token[2])

       if language not in exam_result:
           validate_containing_value(exam_result, username,points, [])
           exam_result.append(language)
