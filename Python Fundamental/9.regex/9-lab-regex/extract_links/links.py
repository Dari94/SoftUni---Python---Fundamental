import re
num = int(input())
for n in range(0,num):
    text = input()

    domain_pattern = r"(w{3}\.[A-Za-z0-9]+\-?[a-z0-9]+\.[a-z]+\.?[a-z]+)"
    matches = re.findall(domain_pattern, text)
    for match in matches:
        print(match)