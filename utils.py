import receipt
import models


LIST_OF_DEVICES = ["Телефон", "Ноутбук", "Телевизор"]
LIST_OF_STATUSES = ["Ремонтируется", "Готов к выдаче", "Выдан клиенту"]
LIST_OF_RECEIPTS = [
    (receipt.Receipt(models.Phone("Телефон", "Xiaomi", "Android", "Не работает динамик"), "15 Марта", "1", "Шушко Антон", LIST_OF_STATUSES[2])),
    (receipt.Receipt(models.TV("Телевизор", "Samsung", "55 дюймов", "Сломан экран"), "23 Декабря", "5", "Сидоров Андрей", LIST_OF_STATUSES[2])),
    (receipt.Receipt(models.Notebook("Ноутбук", "Asus", "Windows 11", "2022", "Не запускается"), "8 Февраля", "5", "Иванов Иван", LIST_OF_STATUSES[2])),
    (receipt.Receipt(models.TV("Телевизор", "LG", "49 дюймов", "Doesn't work"), "1 Мая", "2", "Пыхов Виталий", LIST_OF_STATUSES[2])),
    (receipt.Receipt(models.Phone("Телефон", "Huawei", "Android", "Не работает зарядка"), "22 Июля", "3", "Самарин Максим", LIST_OF_STATUSES[2]))]
LIST_OF_MONTHS = ["Апреля", "Мая", "Марта", "Июня", "Июля", "Августа", "Сентября", "Октября", "Ноября", "Декабря"]
ADMIN_DICT = {"dima1997": ["qwerty123", "Белинский Дмитрий Иванович"], "shushko_ant": ["123321", "Шушко Антон Юрьевич"]}
