import pickle

class Example:
    def __init__(self, value):
        self.value = value

    def __reduce__(self) -> tuple[object, ...]:
        # tuple[Any, ...] в данном контексте — это кортеж произвольной длины с элементами любого типа, 
        #   который используется для передачи данных сериализации.
        # __reduce__ нужен для настройки процесса pickle-сериализации. 
        #   Обычно возвращает кортеж вида (callable, args), чтобы Python знал, как восстановить объект.
        return (int, (self.value,))

# Сериализация
obj = Example("42")
data = pickle.dumps(obj)
print(data)

# Десериализация
new_obj = pickle.loads(data)
print(type(new_obj))  # 42