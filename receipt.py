class Receipt:
    __counter = 0

    def __init__(self, typeofdevice, dateofreceiving, dateofrepair, initials, status):
        self._typeOfDevice = typeofdevice
        self._dateOfReceiving = dateofreceiving
        self._dateOfRepair = dateofrepair
        self._initials = initials
        self._status = status
        Receipt.__counter += 1

    def __str__(self):
        return f"Номер квитанции: {self.__counter}; Тип устройства: {self._typeOfDevice}; Дата получения: " \
               f"{self._dateOfReceiving}; Время на починку: {self._dateOfRepair} дня (дней); ФИО: {self._initials}; Статус готовности: " \
               f"{self._status}"
