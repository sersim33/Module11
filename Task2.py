class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def value(self):
        return self.__x, self.__y

    @value.setter
    def value(self, xy_tuple):
        self.__x, self.__y = xy_tuple

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

# Створення об'єкта Point
point = Point(7, 10)

# Виведення значень x та y
print(point.x)  # 5
print(point.y)  # 10
