# Вам необходимо написать скрипт для анализа данных статистики игрока, который участвует в прогнозах матчей. 
# В качестве входных данных используется файл StatPlayer.txt, содержащий HTML-код 
# веб-страницы с указанной статистикой. Ваша задача состоит в следующем:

# Прочитать файл StatPlayer.txt, содержащий HTML-код веб-страницы.
# Спарсить результаты прогнозов игрока.
# Рассчитать процент угаданных матчей по представленной статистике.
# Вывести процент угаданных матчей в консоль.
# Обратите внимание, что вам следует использовать библиотеку BeautifulSoup для парсинга HTML-кода и выделения необходимой информации.


from bs4 import BeautifulSoup


with open(file="StatPlayer.txt", mode="rt", encoding="utf-8") as file:
    content = file.read()
soup = BeautifulSoup(markup=content, features="html.parser")
predict = soup.find(name="div", attrs={"id": "predict_result_items"})
predict_mark_rs_not = predict.find_all(name="div", class_="predict_mark rs_not")
all_predicts = predict.find_all(name="div", class_="predict_mark")
print(f"{int((1 - (len(predict_mark_rs_not) / len(all_predicts))) * 100)}%")