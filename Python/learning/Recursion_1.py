def factorial(num: int) -> int:
    if num == 1:
        return 1
    return factorial(num - 1) * num

def fibonacci(index):
    num_1, num_2 = 0, 1
    while index != 0:
        fib = num_1 + num_2
        num_1, num_2 = num_2, fib
        index -= 1
    return fib

def check_palindrom(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return check_palindrom(string[1: -1])

print(factorial(4))
print(fibonacci(10))
print(check_palindrom("HALLAH"))
