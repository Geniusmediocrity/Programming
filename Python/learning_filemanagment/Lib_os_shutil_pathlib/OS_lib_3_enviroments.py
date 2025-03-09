import os


os.system("ls") #? выполняет системную команду.(Linux)
print()

"""os.getenv(key) — это удобный способ безопасно получать значения переменных окружения,
особенно когда нужно предусмотреть их отсутствие. 
Она часто используется для работы с конфигурацией приложений и управления секретами."""
username = os.getenv("USER", default=None)  #? получает значение переменной окружения
print(f"Имя пользователя: {username}")
debug = os.getenv("DEBUG")
print(f"debug is: {debug}")
path = os.getenv("PATH")
print(f"Path is: {path}")


"""Как задать переменную окружения?
В командной строке:
#? Linux/macOS :
#* export MY_VAR="my_value"

#? Windows :
#* set MY_VAR=my_value

#? В Python (временно):
#   Можно задать переменную окружения внутри программы:
"""
os.environ["TESTING ENVIRON"] = "It's work!"    #? – устанавливает переменную окружения(временно)
print(os.getenv("TESTING ENVIRON"))

