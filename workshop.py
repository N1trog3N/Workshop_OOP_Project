import receipt
import utils
import models
import random


class Workshop:
    def __init__(self, listofreceipts: list):
        self._listofreceipts = listofreceipts

    @property
    def listofreceipts(self):
        return self._listofreceipts

    def print_receipts(self):
        all_receipts = self.listofreceipts
        # return f"Ваша квитанция: {all_receipts}"
        print(all_receipts)


def create_receipt():
    initials = input("Введите ваше ФИО: ")
    dateofrepair = random.randint(1, 5)
    dayofreceive = random.randint(1, 30)
    dateofreceive = str(dayofreceive) + utils.spacestr + utils.listOfMonths[random.randint(0, 9)]
    status = utils.listOfStatuses[random.randint(0, 2)]

    print("Выберите тип устройства, которое хотите починить: ")
    for i in range(len(utils.listOfDevices)):
        print(f"{i + 1}. {utils.listOfDevices[i]}")
    typeofdevice = utils.listOfDevices[int(input()) - 1]

    brand = input("Введите модель: ")
    description = input("Введите описание поломки: ")

    if typeofdevice == "Телефон":
        os = input("Введите OС: ")
        dev = models.Phone(typeofdevice, brand, os, description)

    if typeofdevice == "Ноутбук":
        os = input("Введите OС: ")
        dateofmanufacturing = input("Введите дату производства: ")
        dev = models.Notebook(typeofdevice, brand, os, dateofmanufacturing, description)

    if typeofdevice == "Телевизор":
        diagonal = int(input("Введите диагональ экрана: "))
        dev = models.TV(typeofdevice, brand, diagonal, description)

    new_receipt = receipt.Receipt(typeofdevice, dateofreceive, dateofrepair, initials, status)
    return new_receipt.__str__()
