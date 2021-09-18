import re
text = input().lower()
search = input().lower()
pattern = rf"\b{search}\b"
match = re.findall(pattern, text)
print(len(match))