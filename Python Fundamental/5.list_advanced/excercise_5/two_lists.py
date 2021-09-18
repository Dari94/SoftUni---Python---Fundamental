words = input().split(', ')
search_word = input()

res_list = [word for word in words if word in search_word]
print(res_list)