def is_palindrome(word):
    return word == word[::-1]


words = input().split()
search_word = input()

palindrome_words = [word for word in words if is_palindrome(word)]
occurrence_count = palindrome_words.count(search_word)

print(palindrome_words)
print(f'Found palindrome {occurrence_count} times')
