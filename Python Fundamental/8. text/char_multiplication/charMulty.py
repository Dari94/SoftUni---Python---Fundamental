strings = input().split(" ")

ord_list_1 = [ord(x) for x in strings[0]]
ord_list_2 = [ord(x) for x in strings[1]]
total_sum = 0

len_ord_list_1 = len(ord_list_1)
len_ord_list_2 = len(ord_list_2)
min_len = min(len_ord_list_1, len_ord_list_2)
max_len = max(len_ord_list_1, len_ord_list_2)
for i in range(max_len):
    if i < min_len:
        total_sum += ord_list_1[i] * ord_list_2[i]
    elif len_ord_list_1 > len_ord_list_2:
        list_n = ord_list_1[i]
        total_sum += list_n
    elif len_ord_list_1 < len_ord_list_2:
        list_n = ord_list_2[i]
        total_sum += list_n


print(total_sum)