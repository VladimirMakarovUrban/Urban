class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        # return object.__new__(cls)
        cls.houses_history.append(args[0])  # Добавляем название дома в историю при создании объекта
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        # self.houses_history.append(name)

    def __del__(self):
        # self.houses_history.remove(self.name)
        # return print(f"{self.name} снесён, но он останется в истории")
        print(f"{self.name} снесён, но он останется в истории")


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3
print(House.houses_history)
