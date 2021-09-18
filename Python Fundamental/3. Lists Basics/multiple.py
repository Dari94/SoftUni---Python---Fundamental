factor = int(input())
count = int(input())
nums = []

for num in list(range(1,count+1)):
    nums.append(int(num)*factor)
print(nums)