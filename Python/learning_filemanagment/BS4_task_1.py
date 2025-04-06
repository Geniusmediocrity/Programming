# Напишите скрипт для парсинга результатов последних двух матчей (финала и матча за 3-е место) 
# Чемпионата Мира 2022, используя данные из текстового файла FootballWorldChampion.txt, 
# доступного в текущей директории. Выведите результат в формате:

# ​​​​​​​Команда_1 счет_1:счет_2 Команда_2
# Команда_3 счет_3:счет_4 Команда_4

from bs4 import BeautifulSoup


with open(file="FootballWorldChampion.txt", mode="rt", encoding="utf-8") as file:
    content = file.read()
soup = BeautifulSoup(markup=content, features="html.parser")


final = soup.find("body")
final = final.find(name="div", class_="page_main_content")
final_teams = final.find(name="a",  class_="game_link")
final_gls = [goal.text for goal in final_teams.find_all(name="div", class_="gls")]
final_teams = final_teams["title"].split(" - ")
print(f"{final_teams[0]} {final_gls[0]}:{final_gls[1]} {final_teams[1]}")

pre_final = soup.find("body")
pre_final = pre_final.find(name="div", class_="page_main_content")
pre_final_teams = pre_final.find(name="a", class_="game_link", attrs={"href": "/games/15292873/"})
pre_final_gls = [goal.text for goal in pre_final_teams.find_all(name="div", class_="gls")]
pre_final_teams = pre_final_teams["title"].split(" - ")
print(f"{pre_final_teams[0]} {pre_final_gls[0]}:{pre_final_gls[1]} {pre_final_teams[1]}")
