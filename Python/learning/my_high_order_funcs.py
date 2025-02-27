def map(func, seq) -> list:
    result = []
    for el in seq:
        result.append(func(el))
    return result


def filter(func, seq) -> bool:  #! функция возращающая bool это !предикат!
    result = []
    for el in seq:
        boolean = bool(func(el))
        if boolean:
            result.append(el)
    return result
    
def checker_filter(num):
    return 20 > num > 0


def reduce(func, seq, start_value=0):
    val = start_value
    for item in seq:
        val = func(val, item)
    return val

def checker_reduce(x: int, y:int) -> int:
    return x * (x + y) / y




print(map(int, ["1", "2", "3"]))
print(filter(checker_filter, [15, 10, 22, 0, -11, 33]))
print(reduce(checker_reduce, [10, 22, 33, 1], 1))