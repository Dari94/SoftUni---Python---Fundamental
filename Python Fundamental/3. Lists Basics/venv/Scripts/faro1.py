string = input().split()
count = int(input())
first_part = string[ :int(len(string)/2)]
second_part =string[int(len(string)/2) : ]

for x in range (count):
       first_part.append([x])
      second_part.append([x+4])
res = [i + j for i, j in zip(first_part,second_part)]
new_list = list(map( (', ') .join, zip(*first_part,*second_part)))
print(str(first_part), second_part, str(res), new_list)



