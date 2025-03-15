import json
from pathlib import Path


path = Path("JSON/eq_data_1_day_m1.json")
with open(file=path, mode="rt", encoding="utf-8") as file:
    data = json.load(file)
# print(json.dumps(data, indent=4))
print()


#? Построение списка всех землетрясений
# Начнем с построения списка, содержащего всю информацию обо всех произошедших землетрясениях:
with open(file=path, mode="rt", encoding="utf-8") as file:
    data = json.load(file)
all_eq_dicts = data['features']
print(f"Всего произошло землетрясений: {len(all_eq_dicts)}")
print()


#? Извлечение магнитуд
# Имея список, содержащий данные по всем землетрясениям,
# мы можем перебрать содержимое списка и извлечь всю необходимую информацию.
# В данном случае это будет магнитуда каждого землетрясения: 
mags = []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)
print("Магнитуды:", end="\n * ")
print(*mags[:10], sep="\n * ")
print()


#? Извлечение данных местоположения
# Данные местоположения хранятся с ключом "geometry".
# В словаре geometry присутствует ключ "coordinates", 
# первыми двумя значениями которого являются долгота и широта. 
# Извлечение данных происходит следующим образом:
coordinates = []
for eq_dict in all_eq_dicts:
    cord = eq_dict["geometry"]["coordinates"][0:2]
    coordinates.append(cord)
print("Координаты:", end="\n * ")
print(*coordinates[:10], sep="\n * ")
print()
