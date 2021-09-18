import re
text = input()
pattern = r"(?<=[^_]_)([a-zA-Z0-9]+)(?=\b)"
match = re.findall(pattern, text)
print(",".join(m for m in match))