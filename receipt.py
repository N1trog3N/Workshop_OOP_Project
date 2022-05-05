class Receipt:
    _counter = 1

    def __init__(self, typeofdevice, dateofreceiving, dateofrepair, initials, status):
        self._typeOfDevice = typeofdevice
        self._dateOfReceiving = dateofreceiving
        self._dateOfRepair = dateofrepair
        self._initials = initials
        self._status = status
        self._number = Receipt._counter
        Receipt._counter += 1

    def __str__(self):
        return f"Номер квитанции: {self._number}; Тип устройства: {self._typeOfDevice}; Дата получения: " \
               f"{self._dateOfReceiving}; Время на починку: {self._dateOfRepair} дня (дней); ФИО: {self._initials}; Статус готовности: " \
               f"{self._status}"
