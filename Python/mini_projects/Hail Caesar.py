upper_eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_eng = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'


def Ceisar(txt):
    list_ = []
    new_text = ''
    for i in range(len(txt)):
        counter = 0
        for k in range(len(txt[i])):
            now_txt = txt[i]
            if now_txt[k].isalpha():
                counter += 1
        for j in range(len(txt[i])):
            now_txt = txt[i]
            if now_txt[j].isalpha():
                if now_txt[j] in lower_eng:
                    index = lower_eng.index(now_txt[j])
                    form = lower_eng
                else:
                    index = upper_eng.index(now_txt[j])
                    form = upper_eng
                new = (index + counter) % 26
                new_text += form[new]
            else:
                new_text += now_txt[j]
        list_.append(new_text)
        new_text = ''
    return list_

text = input('Введите текст для его шифровки\n').split()
print(*Ceisar(text))