import re
pattern = r"(\+359([-| ])2\2[\d]{3}\2[\d]{4}\b)"

text = input()
result = re.findall(pattern,text)
print(", ".join([phone for phone, sep in result]))