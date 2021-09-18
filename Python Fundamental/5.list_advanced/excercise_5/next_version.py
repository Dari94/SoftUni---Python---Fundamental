version = input().split(".")
nums = list(map(int,version))

nums[2] += 1
if nums[2] == 10:
    nums[2] = 0
    nums [1] += 1

if nums[1] == 10:
    nums[1] = 0
    nums[0] += 1
print('.'.join(map(str,nums)))

print(nums)