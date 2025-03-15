import json


with open(file="JSON/eq_data_1_day_m1.json", mode="rt", encoding="utf-8") as file:
    data = json.load(file)["features"]
all_eq = tuple((eq["properties"]["mag"], eq["properties"]["place"]) for eq in data)
print(max(all_eq)[1])
