class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.model = __model
        self.engine_power = __engine_power
        self.color = __color
    def get_model(self):
        print(f'Модель: {self.model}')
    def get_horsepower(self):
        print(f'Мощность двигателя: {self.engine_power}')
    def get_color(self):
        print(f'Цвет: {self.color}')
    def print_info(self):
        print(f'{self.model}, {self.engine_power}, {self.color}, Владелец: , {self.owner}')

    def set_color(self, new_color):
        self.color = new_color
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.get_model()
vehicle1.get_horsepower()
vehicle1.get_color()

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()