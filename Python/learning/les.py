import re



string = "Языки программирования C++, Algol-73, JavaScript-18.0, Python-3.9, Ruby v.6.44."
pattern = r"\w+-\d+.\d?"
print(re.findall(pattern, string))