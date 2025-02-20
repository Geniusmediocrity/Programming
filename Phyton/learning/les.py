string = input()
length = len(string)
if length % 2:
    print(string[length // 2:] + string[: length // 2]) 
else:
    print(string[length // 2:] + string[: length // 2]) 