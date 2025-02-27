with open(file=input(), mode="rt", encoding="utf-8") as file:
    last_line = ""
    res = []
    for line in file.readlines():
        if line.startswith("def ") and "#" not in last_line:
            res.append(line[4: line.index("(")])
        last_line = line
    if not res:
        print("Best Programming Team")
    else:
        print(*res, sep="\n")