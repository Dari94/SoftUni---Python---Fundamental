def solution(string):
   for ch in string:
        string = string.replace(ch * 2, ch)
   return string


if __name__ == '__main__':
    string = input()
    print(solution(string))