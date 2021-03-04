#regex - exam april 2020
import re
pattern = r"\@\#+(?P<bar>[A-Z][A-Za-z0-9]{4,}[A-Z])\@\#+"
num = int(input())

for n in range(num):
    text = input()
    match = re.match(pattern, text)
    if match is None:
        print("Invalid barcode")
    else:
        match = match[1]
        match_split = match.split()

        digits = [c for c in match if c in '0123456789']
        if digits == []:
            print(f"Product group: {'00'}")
        else:
            print(f"Product group: {''.join(digits)}")
