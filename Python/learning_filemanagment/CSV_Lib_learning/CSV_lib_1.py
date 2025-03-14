import csv
from pathlib import Path


data = Path("data.csv").resolve()
#? Для чтения данных из файла программист должен создать объект reader:
#* Методы и атрибуты :
#   __next__(): Возвращает следующую строку как список.
#   __iter__(): Возвращает итератор для перебора всех строк.
#   line_num: Возвращает номер текущей строки (для отладки).
with open(file=data, mode="rt", encoding="utf-8") as file:
    file_reader = csv.reader(file, delimiter=",")
    counter = 0
    for row in file_reader:
        print(row)
        counter += 1
    # print(f"Количество строк в файле: {counter}")
print()
    
#? csv.writer Позволяет записывать данные в CSV-файл.
#? newline='' в open(): Нужен при записи, чтобы избежать лишних пустых строк в Windows.
#* Методы :
#   writerow(row): Записывает одну строку (список).
#   writerows(rows): Записывает несколько строк (список списков).
# with open(file=data, mode="wt", newline="", encoding="utf=8") as file:
#     writer = csv.writer(file, delimiter=",", quoting=csv.QUOTE_MINIMAL)
#     writer.writerows([
#         ['Имя', 'Успеваемость', 'Год рождения'],
#         ['Саша', 'отличник', '200'],
#         ['Маша', 'хорошистка', '1999'],
#         ['Петя', 'троечник', '2000'],
#     ])

#? csv.DictReader Читает CSV-файл и преобразует каждую строку в словарь, где ключи — заголовки столбцов.
#* Методы и атрибуты :
#   fieldnames: Список заголовков (можно задать вручную).
#   __next__(): Возвращает следующую строку как словарь.
with open(file=data, mode="rt", encoding="utf-8") as file:
    dict_reader = csv.DictReader(file)
    print(f"Заголовки: {dict_reader.fieldnames}")
    # print(dict_reader.__next__())
    # print(dict_reader.__next__())
    # print(dict_reader.__next__())
    
#? csv.DictWriter Записывает данные в CSV-файл в виде словарей.
#* Методы :
#   writeheader(): Записывает заголовки (fieldnames).
#   writerow(row_dict): Записывает одну строку (словарь).
#   writerows(rows_list): Записывает список словарей.
with open(file=data, mode="wt", encoding="utf-8") as file:
    fieldnames = ['Имя', 'Возраст', 'Город']
    dict_writer = csv.DictWriter(f=file,  fieldnames=fieldnames, delimiter=",")
    dict_writer.writeheader()
    dict_writer.writerow({'Имя': 'Алексей', 'Возраст': 40, 'Город': 'Казань'})
    