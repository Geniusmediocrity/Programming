import datetime


week_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

def display_events():
    with open(file="events.txt", mode="rt", encoding="utf-8") as event_f, open(file="expect.txt", mode="wt", encoding="utf-8") as expect_f:
        readlines = list(map(lambda el: el.rstrip().split(", "), event_f.readlines()))
        for event, date in readlines:
            res = ""
            year, month, days = date.split("-")
            obj_date = datetime.date(int(year), int(month), int(days))
            res = f'{obj_date.strftime("%A")}, {date}: {event} - Осталось {0} дней'
            print(res, file=expect_f)
            
print(datetime.datetime.now(datetime.timezone.utc))
display_events()