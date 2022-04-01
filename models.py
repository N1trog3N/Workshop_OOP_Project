class Device:

    def __init__(self, type, brand, description):
        self._type = type
        self._brand = brand
        self._description = description

    def __str__(self):
        return f"Устройство: {self._type}, Модель: {self._brand}, Описание: {self._description}"


class Phone(Device):

    def __init__(self, type, brand, os, description):
        super(Phone, self).__init__(type, brand, description)
        self._os = os

    def __str__(self):
        return f"{self._type}\n{super().__str__()}, OS: {self._os}"


class Notebook(Device):

    def __init__(self, type, brand, os, dateofmanufacturing, description):
        super(Notebook, self).__init__(type, brand, description)
        self._dateofmanufacturing = dateofmanufacturing
        self._os = os

    def __str__(self):
        return f"{self._type}\n{super().__str__()}, OС: {self._os}, Дата выпуска: {self._dateofmanufacturing}"


class TV(Device):

    def __init__(self, type, brand, diagonal, description):
        super(TV, self).__init__(type, brand, description)
        self._diagonal = diagonal

    def __str__(self):
        return f"{self._type}\n{super().__str__()}, Диагональ экрана: {self._diagonal}"
