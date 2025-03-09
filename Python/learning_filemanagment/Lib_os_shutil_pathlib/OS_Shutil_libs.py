import time
import os
import shutil
from pathlib import Path


# ?    Метод	                                Описание
# -------------------+---------------------------------------------------------------|
#   shutil.copyfile()	                Копирует содержимое одного файла в другой.
#   shutil.copy()	                Копирует файл вместе с его правами доступа.
#   shutil.copymode()                   Копирует права доступа (режим доступа) с одного файла (src) на другой файл (dst).
#                                  Она не копирует содержимое файла или метаданные, такие как владельцы или временные метки — только права доступа.

#   shutil.move()	                Перемещает файл в другую директорию и удаляет исходный.
#   os.rename()	                        Переименовывает файл.
#   os.remove()	                        Удаляет указанный файл.
#   os.path.exists()/Path.exists()      Проверяет существование файла или директории.
#   os.path.getsize()	                Возвращает размер файла в байтах.
#   os.path.getatime()	                Определяет время последнего доступа к файлу.
#   os.path.getctime()	                Возвращает дату создания файла.
#   os.path.getmtime()	                Показывает время последнего изменения файла.

def make_new_file():
    new_file = Path("testing.py")
    new_file.touch()


# ? Копирование содержимого одного файла в другой
shutil.copyfile("constrains.txt", "txt_files/data.txt")
# ? Копирование файла с сохранением прав доступа
shutil.copy("constrains.txt", "txt_files/data.txt")
shutil.copymode(".venv", "figure")  # ? Копирует права доступа (режим доступа)
"""
Как это работает?(copymode)
        Функция считывает режим доступа (permissions) исходного файла (src) с помощью os.stat.
        Затем она применяет этот режим к целевому файлу (dst) с помощью os.chmod.
"""
# ? Копирует не только права доступа, но и другие метаданные, такие как время последнего доступа и изменения:
shutil.copystat("OS_lib_2_rmtree.py", "testing.py")
# ? Если вам нужно явно установить права доступа, используйте os.chmod:
os.chmod("OS_Shutil_libs.py", 0o766)
print("OS_Shutil_libs.py mode:", oct(
    os.stat("OS_Shutil_libs.py").st_mode)[-3:])    # Выведет: '766'
# shutil.copyfile("requirements.txt", "file_1.txt")
# shutil.copy("requirements.txt", "file_1.txt")
# shutil.copymode("requirements.txt", "file_1.txt")
# shutil.copystat("requirements.txt", "txt_files/data.txt")
# shutil.move("testing.py", "txt_files")

make_new_file()
time.sleep(3)
os.rename("testing.py", "new_testing.py")
os.remove("new_testing.py")
# os.mknod("new_testimg.py")      #! только на Unix
make_new_file()
print()
print(f"Get size file: {os.path.getsize("testing.py") = }")   # Возвращает размер файла в байтах.
print(f"Get acces time: {os.path.getatime("testing.py") = }")    # Определяет время последнего доступа к файлу.
print(f"Get create time: {os.path.getctime("testing.py") = }")    # Возвращает дату создания файла.
print(f"Get madificate time: {os.path.getmtime("testing.py")}")    # Показывает время последнего изменения файла.