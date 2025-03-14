import csv
import datetime


csv.register_dialect("csv_dialect", delimiter=",", lineterminator="\r")

with open(file="dates_arrival.txt", mode="rt", encoding="utf-8") as arrival,\
open(file="dates_departure.txt", mode="rt", encoding="utf-8") as departure,\
open(file="result.csv", mode="wt", encoding="utf-8") as result:
    fieldnames = ["Дата прилета", "Дата убытия", "Количество дней"]
    
    writer = csv.DictWriter(result, fieldnames=fieldnames, dialect="csv_dialect")
    writer.writeheader()
    
    for ar, dep in zip(arrival, departure):
        ar, dep = ar.strip(), dep.strip()
        
        day_ar, month_ar, year_ar = tuple(map(int, ar.split("-")))
        day_dep, month_dep, year_dep = tuple(map(int, dep.split("-")))
        
        days_counter = datetime.date(year_dep, month_dep, day_dep) - datetime.date(year_ar, month_ar, day_ar)
        writer.writerow({"Дата прилета": ar, "Дата убытия": dep, "Количество дней": days_counter.days})
