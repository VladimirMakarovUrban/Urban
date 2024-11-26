class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        print("Дом: ", name, 'Количество этажей: ', number_of_floors)
    def go_to(self, new_floor):
        if new_floor <= self.number_of_floors:
            for i in range(1, new_floor+1):
                print(i)
        else:
            print("Такого этажа не существует")


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
fl = int(input('На какой этаж поедем? '))
h1.go_to(fl)
h2.go_to(fl)
