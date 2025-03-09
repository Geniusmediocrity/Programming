import csv


#? Для чтения данных из файла программист должен создать объект reader:
with open(file="data.csv", mode="rt", encoding="utf-8") as file:
    file_reader = csv.reader(file, delimiter=",")
    counter = 0
    for row in file_reader:
        print(row) 