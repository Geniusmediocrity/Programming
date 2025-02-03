new_list = []
umnozhenie = 1
for i in range(10):
    vvod = [int(input(f'Введите {i+1} любое целое число : '))]
    new_list +=vvod
new_list.sort(key=abs,reverse=True)
print ('Список: ',new_list)
for i in range (len(new_list)):
    if i % 2 ==0:
        if new_list[i] % 3 == 0:
            umnozhenie *=new_list[i]
print (umnozhenie)