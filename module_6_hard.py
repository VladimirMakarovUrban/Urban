class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = self.__validate_color(color)
        self.__sides = self.__validate_sides(*sides)
        self.filled = True

    def __validate_color(self, color):
        r, g, b = color
        if self.__is_valid_color(r, g, b):
            return [r, g, b]
        else:
            return [255, 255, 255]

    def __is_valid_color(self, r, g, b):
        return all(0 <= x <= 255 and isinstance(x, int) for x in (r, g, b))

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __validate_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            return list(sides)
        else:
            return [1] * self.sides_count

    def __is_valid_sides(self, *sides):
        return len(sides) == self.sides_count and all(isinstance(x, int) and x > 0 for x in sides)

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius):
        super().__init__(color, int(2 * 3.14 * radius))
        self.__radius = radius

    def get_square(self):
        return 3.14 * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a, b, c = self.__sides
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length):
        super().__init__(color, side_length, side_length, side_length, side_length, side_length, side_length,
                         side_length, side_length, side_length, side_length, side_length, side_length)

    def get_volume(self):
        return self._Figure__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())
# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
# Проверка периметра (круга), это и есть длина:
print(len(circle1))
# Проверка объёма (куба):
print(cube1.get_volume())
