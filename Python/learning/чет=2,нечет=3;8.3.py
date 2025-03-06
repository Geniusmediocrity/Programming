natural_number = int(input())
max_num = 0
min_num = 10
while natural_number != 0:
    new_num = natural_number % 10
    if new_num > max_num:
        max_num = new_num
    if min_num > new_num < max_num or min_num == 0:
        min_num = new_num
print(f'Максимальная цифра равна {max_num}')
print(f'Минимальная цифра равна {min_num}')