import os
import time
from icecream import ic


print(f"System type [os.name]: {os.name}")    #? Тип системы
print(f"Get Current working directory [os.getcwd()]: {os.getcwd()}")    #? Текущая директория
#TODO   print(f"Change directory [os.chdir('/home/alexy')]: {os.chdir("/home/alexy")}. dir now: {os.getcwd()}")     #? Изменение рабочей директории
print(f"Проверка существования пути [os.path.exists('')]: {os.path.exists("test")}")    #? Проверка существования пути
print(f"Полный путь к файлу [os.path.abspath('learning_filemanagment']: {os.path.abspath("learning_filemanagment")}")    #? Полный путь к файлу
print(f"Проверка файла [os.path.isfile('files.py')]: {os.path.isfile('files.py')}")    #? Проверка файла
print(f"Проверка директории [os.path.isdir('test')]: {os.path.isdir('test')}")

#!  os.startfile("txt_file/logfile.txt")    # на линуксе не работает

os.mkdir("Test_dir")
ic("check catalog")
for i in range(3):
    print(f"\rProgramm stopped {i}", end="")
    time.sleep(1)
print()
os.rmdir("Test_dir")
print("Test_dir was succesful remove")

ic("check catalog")
os.mknod("test.txt")
for i in range(3):
    print(f"\rProgramm stoped {i}", end="")
    time.sleep(1)
os.remove("test.txt")
print("test.txt was succesfully denied")

#TODO   os.chdir('./11.Алексей/Programming/Python/learning_filemanagment')
print(os.path.exists('test_os.txt'))
#TODO   os.rename("new.txt", "test_os.txt")
#TODO   os.remove("t.txt")
now_dir = os.getcwd()
#TODO   os.mkdir("new_test")

print(f'os.path.basename() = {os.path.basename(f"{now_dir}/files.py")}')    #? Используется для извлечения имени файла или последнего компонента пути из полного пути к файлу или директории.
print(f'os.path.dirname() = {os.path.dirname(f"{now_dir}/files.py")}')    #? Получить путь к файлу без названия
catalog, f = os.path.split(f"{now_dir}/files.py")   #? Разделить имя файла и путь
print(f"{f = }, {catalog = }")     
print(f"join catalog & f:{os.path.join(catalog, f)}")
print(f"files size(os.path.getsize()): {os.path.getsize('.venv')} bytes")
print()
print("os.listdir(now_dir):")
for dir_el in os.listdir(now_dir):
    ic(dir_el)
    
    
"""Функция os.walk возвращает генератор, который на каждой итерации выдает кортеж из трех элементов:

Путь к текущей директории (root) — строка с полным путем к текущей папке.
Список подкаталогов (dirs) — список имен подкаталогов в текущей директории.
Список файлов (files) — список имен файлов в текущей директории."""

files_counter = 0
for root, dirs, files in os.walk("./"): #? На каждой итерации:
    files_counter += len(files)
    # print(f"Текущая директория: {root}")    #? root содержит путь к текущей директории.
    # print(f"Подкаталоги: {dirs}")           #? dirs содержит список подкаталогов в этой директории.
    # print(f"Файлы: {files}")                #? files содержит список файлов в этой директории.
    # print("-" * 40)           #? Обход продолжается рекурсивно для всех подкаталогов.
print(f"Общее количество файлов: {files_counter}")
