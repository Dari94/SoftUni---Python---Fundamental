n_people = int(input())
p_capacity = int(input())
import math
courses = math.ceil(n_people / p_capacity)
if n_people % p_capacity == 0:
    print(int((n_people/p_capacity)))
else:
    print(int(courses))