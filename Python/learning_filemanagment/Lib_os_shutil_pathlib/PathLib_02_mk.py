import os
import time
import shutil
from pathlib import Path
#! Pathlib стоит использовать только для работы путями
#! Для работы с переменными окружениями необходимо использовать модкль os


# 1:
try:
    p = Path("TempDir")
    p.mkdir()
    time.sleep(3)
    print("succes 1")
except Exception as e:
    print(e)
finally:
    p.rmdir()   #? удаляет только пустой каталог

# 2:
try:
    p = Path("TempDir/Subdir")
    p.mkdir(parents=True)
    time.sleep(3)
    print("succes 2")
except Exception as e:
    print(e)
finally:
    shutil.rmtree(p.parent)
    
# 3:
p = Path("tempfile.txt")
#TODO:   p.rename("tempfile.txt")
time.sleep(2)
p.unlink()
print("acces 3")