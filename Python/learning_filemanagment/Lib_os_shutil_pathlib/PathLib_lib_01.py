import os
import pathlib as pth
from icecream import ic


print(pth.Path().cwd())

# for p in pth.Path().iterdir():
#    print(p)

my_dir = pth.Path("Directory_1")
my_file = pth.Path("file_1.txt")

new_file = my_dir / "new_file.txt"
new_file_2 = my_dir.joinpath("new_file_2.txt")

print(type(my_dir))
print(type(my_file))
print()
print(f"Dir name: {my_dir.name}")
print(f"File name: {my_file.name}")
print()
print(f"Dir suffix(расширение): {my_dir.suffix}")
print(f"File suffix(расширение): {my_file.suffix}")
print()
print(f"Имя без расширения: {my_dir.stem}")
print(f"Имя без расширения: {my_file.stem}")
print()
print(new_file)
print(new_file_2)
print()
print(f"Is my_dir exists?:  {my_dir.exists()}")
print(f"Is my_file exists?:  {my_file.exists()}")
print(f"Is new_file exists?:  {new_file.exists()}")
print(f"Is new_file_2 exists?:  {new_file_2.exists()}")
print()
print(f"The parent of my_dir is: {my_dir.parent}")
print(f"The parent of my_file is: {my_file.parent}")
print(f"The parent of new_file is: {new_file.parent}")
print(f"Parents parent of new_file is: {new_file.parent.parent}")
print()
print(f"Absolute path of my_dir: {my_dir.absolute()}")
print(f"Absolute path of parent my_dir: {my_dir.parent.absolute()}")
print(f"Absolute path of my_file: {my_file.absolute()}")
print(f"Absolute path of new_file: {new_file.absolute()}")
print()
p = pth.Path("..")
print(f"Absolute of p: {p.absolute()}")
print(f"Resolve of p: {p.resolve()}")
print(f"Абсолютный путь к данному скрипту: {pth.Path(__file__)}")
print()
home = pth.Path("~").expanduser()   #? выполняет переход в различный каталоги НЕ относительно текущего
print(f"home cata: {home}")
home = pth.Path.home()
print(f"Home cata: {home}")
print()

presentations = pth.Path("C:\\11.Алексей\презентации\Информатика")
#?  .globs() -- перебирает все файлы в указанном пути
#?  .globs(pattern: str,     : паттерн для поиска файлов только по определенным параметрам
#?  *,
#?  case_sensitive: bool | None = None,     : чувствительность к регистру
#?  recurse_symlinks: bool = False)      : recuse_symlinks
for file in presentations.glob("*.docx"): #? * -- символ подстановки, ищем все файлы в названии которых в конце присутствует .docx
    ic(file)
print()

#? .rglob()[os.walk()] -- перебирает рекурсивно все файлы и папки в указанном каталоге 
for file in pth.Path("figure").rglob("__pycache__"):
    ic(file)
    
print(f"\n{'-' * 100}\n")

json_data = pth.Path().cwd() / "my_json.json"
with json_data.open() as json:  # = open(json_data) as json
    print(json.read())
    
