companions = int(input())
days = int(input())
coins = 0
days_count = 1
import math

while days >= days_count:

    if days_count % 10 == 0:
        companions -= 2

    if days_count % 15 ==0:
         companions += 5

    if days_count % 3 == 0:
        coins -= 3 * companions

    if days_count % 5 == 0:
        coins += 20 * companions

    if days_count % 5 == 0 and days_count % 3 == 0:
        coins -= 2 * companions


    days_count += 1
    coins += 50 - 2 * companions

coins = int(math.floor(coins/ companions))
print(f'{companions} companions received {coins} coins each.')