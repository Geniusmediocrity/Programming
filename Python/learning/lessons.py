import re

from icecream import ic


string = "text sjdbndzkTEXT fff TeXT TexT ryegirug"
pattern = r"text"
result = re.findall(pattern, string, flags=re.IGNORECASE)
ic(result)

string = """The sky is blue.
The grass is green.
The apple is red.
Bananas are yellow."""
pattern = r"green|blue"
result = re.findall(pattern, string, flags=re.MULTILINE)
ic(result)

pattern = r"\b\w+\b"
r"""Регулярное выражение r'\b\w+\b' используется для поиска отдельных слов в тексте. Оно находит:
--  Последовательности символов, которые состоят из букв, цифр или подчеркиваний (\w+),
--  При этом эти последовательности должны быть ограничены границами слов (\b)."""
string = "Hello Привет"
result = re.findall(pattern, string, flags=re.ASCII)
ic(result)

"""import locale
locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")
text = "Привет мир 123"
pattern = r"\w+"
ic(re.findall(pattern, text))
print(re.findall(pattern, text, flags=re.LOCALE))"""

text = """Привет
МИР"""
pattern = r".+"
ic(re.findall(pattern, text,))  # ['Привет', 'МИР']
print(re.findall(pattern, text, flags=re.DOTALL))  # ['Привет\nМИР']

text = "(123) 456-7890"
pattern = r"""
    \(\d{3}\)    # Код региона в скобках
    \s?          # Пробел (необязательный)
    \d{3}        # Первые три цифры
    -            # Тире
    \d{4}        # Последние четыре цифры
"""
match = re.match(pattern, text, flags=re.VERBOSE)
print(match.group())

pattern = re.compile(r'\d+', re.DEBUG)

text = "12345"

matches = pattern.findall(text)

print(matches)  # ['12345']

"""
Когда вы выполните этот код, Python выведет подробную информацию о том,
как оно компилирует регулярное выражение. Пример вывода может выглядеть так:


at position 0
  in <string>: \d+
    LITERAL 48
    LITERAL 57
"""