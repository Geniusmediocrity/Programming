sp = list(input ('Введите строку '))
rem_sp = list(input ('Введите элементы которые надо удалитьиз строки '))
for r in rem_sp :
    for i in sp:
        if sp.count(r) > 0:
                sp.remove(r)
print (sp)