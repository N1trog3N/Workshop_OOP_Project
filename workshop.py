import receipt
import utils
import models
import random


class Workshop:
    def __init__(self, listofreceipts: list):
        self._listofreceipts = listofreceipts

    def print_receipts(self):
        all_receipts = self._listofreceipts
        return all_receipts

    def create_receipt(self):
        initials = input("Введите ваше ФИО: ")
        dateofrepair = random.randint(1, 5)
        dayofreceive = random.randint(1, 30)
        dateofreceive = f"{dayofreceive} {utils.LIST_OF_MONTHS[random.randint(0, 9)]}"
        status = utils.LIST_OF_STATUSES[random.randint(0, 2)]

        print("Выберите тип устройства, которое хотите починить: ")
        for i in range(len(utils.LIST_OF_DEVICES)):
            print(f"{i + 1}. {utils.LIST_OF_DEVICES[i]}")
        typeofdevice = utils.LIST_OF_DEVICES[int(input()) - 1]

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
        self._listofreceipts.append(new_receipt)
