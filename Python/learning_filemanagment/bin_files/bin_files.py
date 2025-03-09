import pickle
import struct


books = [
("Евгений Онегин", "Пушкин А.С.", 200),
("Муму", "Тургенев И.С.", 250),
("Мастер и Маргарита", "Булгаков М.А.", 500),
("Мертвые души", "Гоголь Н.В.", 190)
]
with open(file="out.bin", mode="wb") as binary:
    pickle.dump(books, binary)  #? pickle.dump(откуда считывать, куда записывать)
    
with open(file="out.bin", mode="rb") as binary:
    print(pickle.load(binary))
    
    
book_1 = ("Евгений Онегин", "Пушкин А.С.", 200)
book_2 = ("Муму", "Тургенев И.С.", 250)
book_3 = ("Мастер и Маргарита", "Булгаков М.А.", 500)
book_4 = ("Мертвые души", "Гоголь Н.В.", 190)
with open("out.bin", mode="wb") as binary:
    pickle.dump(book_1, binary)
    pickle.dump(book_2, binary)
    pickle.dump(book_3, binary)
    pickle.dump(book_4, binary)

with open(file="out.bin", mode="rb") as binary:
    for _ in range(4):
        print(pickle.load(binary))
        
with open(file="out_2.bin", mode="wb") as binary:
    data = struct.pack("iif", 1, 2, 3.14)
    binary.write(data)
with open(file="out_2.bin", mode="rb") as binary:
    data = binary.read()
    data = struct.unpack("iif", data)
    print(data)
