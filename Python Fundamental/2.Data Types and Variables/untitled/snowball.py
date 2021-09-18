snowball_num = int(input())

max_value = 0
last_time = 0
last_snow = 0
last_quality = 0
for i in range(1,snowball_num+1):

    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = pow(int(snowball_snow / snowball_time), snowball_quality)

    if snowball_value > max_value:
        max_value = snowball_value
        last_time = snowball_time
        last_snow = snowball_snow
        last_quality = snowball_quality


print(f'{last_snow} : {last_time} = {max_value} ({last_quality})')