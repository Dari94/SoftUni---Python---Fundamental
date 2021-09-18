words = input().split()
search_word = input()
palindromes = []

for word in words:
    if word == "".join(reversed(word)):
        palindromes.append(word)

occurrence_count = palindromes.count(search_word)
print(f'{palindromes}')
print(f'Found palindrome {occurrence_count} times')