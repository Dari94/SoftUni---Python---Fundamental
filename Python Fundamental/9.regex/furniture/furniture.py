import re
total_sum = 0
print("Bought furniture:")
while True:
    text = input()
    if text == "Purchase":
        print(f"Total money spend:{total_sum: .2f}")
        break
    pattern = r">>([a-zA-Z]+)<<(\d+\.?\d*)!(\d+)"
    matches = re.findall(pattern, text)
    for match in matches:
        print(match[0])
        total_sum += float(match[1]) * int(match[2])