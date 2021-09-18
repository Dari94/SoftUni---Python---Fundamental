
employees = input().split(" ")
factor = int(input())
employees_happiness = [int(happiness) for happiness in employees]

factored_employees_happiness = list(map(lambda h: int(h) * factor, employees_happiness))
average_happiness = sum(factored_employees_happiness) / len(factored_employees_happiness)
happy_employees = [e for e in factored_employees_happiness if e >= average_happiness]
unhappy_employees = [e for e in factored_employees_happiness if e < average_happiness]

if len(happy_employees) >= len(unhappy_employees):
    print(f'Score: {len(happy_employees)}/{len(employees_happiness)}. Employees are happy!')
else:
    print(f'Score: {len(happy_employees)}/{len(employees_happiness)}. Employees are not happy!')