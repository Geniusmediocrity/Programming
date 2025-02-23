def check_time(start, finish) -> int:
    hour_1, min_1 = start.split(":")
    hour_2, min_2 = finish.split(":")
    hour_1, min_1, hour_2, min_2 = int(hour_1), int(min_1), int(hour_2), int(min_2)
    return (hour_2 * 60 + min_2) - (hour_1 * 60 + min_1) >= 60


with open(file="logfile.txt", mode="rt", encoding="utf-8") as log, open(file="output.txt", mode="wt", encoding="utf-8") as out:
    logs = [el.split(", ") for el in list(log)]
    pupils = [name for name, start, finish in logs if check_time(start, finish.rstrip())]
    print(*pupils, sep="\n", file=out)
