def max_len(seq: tuple|list|str, start: int) -> int:
    """Возращает максимальную длинну последовательности в зависимости от начальной позиции.add()
    Пояснение: берет куски последовательности(срезами) и смотрит являются ли они AB или CB 
    да:
        +1 к длинне
    нет:
        заносит уже зафиксированную длинну последовательности в список результатов
    Возвращает максимальную длинну последовательности 
    """
    result = []
    counter = 0
    while start < len(seq) - 1:
        if seq[start: start + 2] in ("AB", "CB"):
            counter += 1
        else:
            result.append(counter)
            counter = 0
        start += 2
    return max(result)
        
        

def main(path: str, encoding="utf-8"):
    with open(file=path, mode="rt", encoding=encoding) as file:
        read_file = file.read()
        #? определение максимальной длинны при страте с 0 и 1:
        return (max(max_len(read_file, 0), max_len(read_file, 1)))


result = main(path="Practice/Задание 6.txt")
print(result)
#? среднее время выполнения программы: 1.79725с

# ----------------------------------------------------------------------------------

def max_len(seq: str|list|tuple) -> int:
    start = 0
    result = []
    last_symb = seq[0]
    counter = 0
    while start < len(seq) - 1:
        if seq[start: start + 2] in "AB CB":
            counter += 1
            start += 2
        else:
            start += 1
            result.append(counter)
            counter = 0
    return max(result)
        
        

def main(path: str, encoding="utf-8"):
    with open(file=path, mode="rt", encoding=encoding) as file:
        read_file = file.read()
        return max_len(read_file)


result = main(path="Practice/Задание 6.txt")
print(result)
#? Среднее время выполнения программы: 0.9849000000000001с что в 2 раза быстрее(если кортеж)
#? Если строка: ~0.8989889328с, что на 10 секунд меньше по времени выполнения