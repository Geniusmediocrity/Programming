a = [1, 2, 3]

b = {1: 100, 2: 200}

try:

    print(b[4])

    print(a[5])

except (KeyError, IndexError) as e:

    print(type(e)) # <class 'KeyError'>

    print(e) # 4