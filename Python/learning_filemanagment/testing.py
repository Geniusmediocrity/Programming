import datetime


def display_events():
    week_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    with open(file="events.txt", mode="rt", encoding="utf-8") as event_f, open(file="expect.txt", mode="wt", encoding="utf-8") as expect_f:
        readlines = list(map(lambda el: el.rstrip().split(", "), event_f.readlines()))
        counter = len(readlines)
        for event, date in readlines:
            counter -= 1
            res = ""
            year, month, days = date.split("-")
            obj_date = datetime.date(int(year), int(month), int(days))
            time_delta = abs((datetime.date.today() - obj_date).days)
            res = f'{week_days[obj_date.weekday()]}, {date}: {event} - Осталось {time_delta} дней'
            if counter != 0:
                expect_f.write(f"{res}\n")
            else:
                expect_f.write(f"{res}")
        
            

display_events()
