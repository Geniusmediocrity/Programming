
#!                          Задача #1🌟
#? Напишите функцию , которая анализирует лог-файл. Каждый лог состоит из строки с датой, временем и сообщением. Программа должна:
#   Прочитать лог-файл.
#   Подсчитать, сколько раз встречаются сообщения с определённым уровнем важности (например, "ERROR", "WARNING", "INFO").
#   Записать в новый файл строки, содержащие сообщения с уровнем "ERROR", отсортированные по времени.

errors, warnings, info = 0, 0, 0
with open("Files_tasks/t_1/logs.txt", mode="rt", encoding="utf-8") as file,\
open("Files_tasks/t_1/error_logs_sorted.txt", mode="wt", encoding="utf-8") as result:
    for line in file.readlines():
        if "ERROR" in line:
            result.write(line)
            errors += 1
        warnings += 0 if "WARNING" not in line else 1
        info += 0 if "INFO" not in line else 1
print(f"""{errors = }
{warnings = }
{info = }""")