string = input()
emoticons ="\n".join([string[i:i+2] for i in range(len(string)) if string[i] == ":" ])
print(emoticons)