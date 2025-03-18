import re


def get_email(string):
    pattern = r"\b\w+@[\w\.]+\w+\b"
    return re.search(pattern, string).group()


text = "Please contact alexeykozhakin@yan.3dex.ru............... for assistance"
print(get_email(text))