def smallest(a,b,c):
    if a<b and a<c:
        return a
    if b<a and b<c:
        return b
    if c<a and c<b:
        return  c


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

print(smallest(num_1,num_2,num_3))