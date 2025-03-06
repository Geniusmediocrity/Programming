import random

'''Функции'''
def start():
    """Началло игры"""
    print('Добро пожаловать в числовую угадайку')
    mark = True
    while mark:
        guessing_game()
        print('\n', '-' * 100, '\n')
        question = input('Желаете продолжить игру?(Да/Yes")  ')
        if question.lower() not in 'yesда':
            print('Досвидвния надеюсь еще увидимся вновь!')
            break

def foolproof(num):
    """Защита от дурака"""
    while not num.isdigit():
        print('Ошибка ввода... Введено неверное значени')
        num = input('Введите значение снова:  ')
    return int(num)
    
def guessing_game():
    """Логика игры"""
    print('Введите диапозон значений для генерации рандомного числа:')
    x, y = int(input('от: ')), int(input('до: '))
    guessing_num = random.randint(x, y)
    
    attemps = 0
    while True: # Основной цикл
        users_num = input('Введите значение:  ')
        users_num = foolproof(users_num)
        if users_num > guessing_num:
            print('Введеное значение больше...')
        elif users_num < guessing_num:
            print('Введеное значение меньше...')
        else:
            print('Поздравляю вы угадали !!!')
            print(f'Количество попыток: {attemps}')
            break
        attemps += 1
    
    
start()