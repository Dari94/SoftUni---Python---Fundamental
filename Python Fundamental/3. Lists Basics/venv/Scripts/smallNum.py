	#function to find n largest element
def smallest_ele(m,n):
    t=[]
    for i in range(n):
        t.append(min(m))#append min of list in a new list
        m.remove(min(m))#remove min of list from the list
    print(m)


num_str = input().split()
n=int(input())

m = []
for num in num_str:
    m.append(int(num))
smallest_ele(m,n)
