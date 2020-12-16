num_heroes = int(input())
heroes = {}
for _ in range(num_heroes):
    hero = input().split(' ')
    name = hero[0]
    hit_points = int(hero[1])
    max_points = int(hero[2])
    if hit_points <= 100 and max_points <= 200:
        heroes[name] = {'HP': hit_points, 'MP': max_points}
    else:
        break
command = input()
while command != 'End':
    arg = command.split(' - ')
    current_command = arg[0]
    name = arg[1]
    if current_command == 'CastSpell':
        mp_needed = int(arg[2])
        spell_name = arg[3]
        if heroes[name]['MP'] >= mp_needed:
            heroes[name]['MP'] -= mp_needed
            left_mp = heroes[name]['MP']
            print(f"{name} has successfully cast {spell_name} and now has {left_mp} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")
    elif current_command == 'TakeDamage':
        damage = int(arg[2])
        attacker = arg[3]
        heroes[name]['HP'] -= damage
        left_hp = heroes[name]['HP']
        if heroes[name]['HP'] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {left_hp} HP left!")
        else:
            heroes.pop(name)
            print(f"{name} has been killed by {attacker}!")
    elif current_command == 'Recharge':
        amount = int(arg[2])
        left_amount = 200 - heroes[name]['MP']
        heroes[name]['MP'] += amount

        if heroes[name]['MP'] >= 200:
            heroes[name]['MP'] = 200
            print(f"{name} recharged for {left_amount} MP!")
        else:
            print(f"{name} recharged for {amount} MP!")

    elif current_command == 'Heal':
        amount = int(arg[2])
        left_amount = 100 - heroes[name]['HP']
        heroes[name]['HP'] += amount

        if heroes[name]['HP'] >= 100:
            heroes[name]['HP'] = 100
            print(f"{name} healed for {left_amount} HP!")
        else:
            print(f"{name} healed for {amount} HP!")

    command = input()

sort_heroes =dict(sorted(heroes.items(), key = lambda x:(-x[1]['HP'],x[0])))
for name, hp_mp in sort_heroes.items():
    user = name
    current_hp = hp_mp['HP']
    current_mp = hp_mp['MP']
    print(f"{user}\n  HP: {current_hp}\n  MP: {current_mp}")
