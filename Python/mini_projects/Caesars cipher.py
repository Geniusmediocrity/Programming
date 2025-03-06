# Описание проекта: требуется написать программу, способную шифровать и дешифровать текст в соответствии с алгоритмом Цезаря. Она должна запрашивать у пользователя следующие данные:
# направление: шифрование или дешифрование;
# язык алфавита: русский или английский;
# шаг сдвига (со сдвигом вправо).
from termcolor import colored 


upper_rus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
lower_rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
upper_eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_eng = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'


def defrator():
    pass


def redefrator():
    pass


def shift():
    question = input('На сколько символов сдвигать буквы по алфавиту?\n')
    while not question.isdigit():
        question = input('Вы ввели неверный формат входных данных. Повторите ввод снова. Введите: число а не что-то другое\n')
    return int(question)

def lang_check():
    question = input('Выберите язык ввода текста( eng/енг или ру/ru )\n')
    while question not in 'engruруенг':
        question = input('Вы ввели неверный формат входных данных. Повторите ввод снова. Введите: eng/енг или ру/ru\n')
    return question


def kind():
    quest = input('Выберите направление: 1) Шифратор; 2) Дешифратор. Введите только номер направления\n')
    while quest != '1' and quest != '2':
        quest = input('Вы ввели неверный формат входных данных. Повторите ввод снова. Введите: 1 или 2\n')
    return int(quest)


def text():
    txt = input('Введите текст который надо использовать?\n')
    while txt.isspace():
        txt = input('Вы ввели неверный формат входных данных. Повторите ввод снова. Введите: текст, а не путое пространство\n')
    return txt


def command():
    lang = lang_check()
    kind_ = kind()
    step = shift()
    txt = text()
    if lang in 'engенг':
        symbs = 26
        upper_txt = upper_eng
        lower_txt = lower_eng
    elif lang in 'rusру':
        symbs = 32
        upper_txt = upper_rus
        lower_txt = lower_rus
    new_txt = ''
    for i in range(len(txt)):
        if txt[i].isalpha():
            if txt[i] in lower_txt:
                format = lower_txt
                index = format.index(txt[i])
            elif txt[i] in upper_txt:
                format = upper_txt
                index = format.index(txt[i])
            if kind_ == 1:
                new_index = (index + step) % symbs
            if kind_ == 2:
                new_index = abs((index - step) % symbs)
            new_txt += format[new_index]
        else:
            new_txt += txt[i]
    print('', '-' * 100, '', colored(f'Результат: ', 'yellow') + new_txt, '', sep='\n')
    


command()