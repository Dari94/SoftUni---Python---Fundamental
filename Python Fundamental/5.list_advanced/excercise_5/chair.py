rooms = int(input())

count = 1
free_chair = 0
while count <= rooms:
    chairs = input().split(' ')
    num_chairs = len(chairs[0])
    taken_places = int(chairs[1])
    diff = num_chairs - taken_places
    free_chair += diff
    if diff < 0:
        print(f'{-diff} more chairs needed in room {count}')

    count += 1

total = free_chair
if total >=0:
   print(f'Game On, {total} free chairs left')

