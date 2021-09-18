
def password (string):
    return '\n'.join([c for c in string if 3 <= len(c) <= 16 and (c.isalnum() and "@" not in c or "_" in c or "-" in c)])
def solution(string):
    print(password(string))
if __name__ == "__main__":
    solution(input().split(", "))