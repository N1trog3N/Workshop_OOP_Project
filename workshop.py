import receipt
import utils
import models
import random


class Workshop:
    def __init__(self, listofreceipts: list):
        self._listofreceipts = listofreceipts

    def print_receipts(self):
        print("\nЧтобы просмотреть информацию о квитанциях, введите номер квитанции или Ваше ФИО:")
        print("1. Ввести ФИО")
        print("2. Ввести номер квитанции")
        sw = int(input())

        if sw == 1:
            info = input("Введите ваше ФИО: ")
            found = False
            for i in self._listofreceipts:
                if i._initials == info:
                    found = True
                    print(i)

            if not found:
                print("Квитанций на Ваше имя не найдено. Попробуйте ещё раз.")

        elif sw == 2:
            info = int(input("Введите номер квитанции: "))
            found = False
            for i in self._listofreceipts:
                if i._number == info:
                    found = True
                    print(i)

            if not found:
                print("Квитанций с таким номером не найдено. Попробуйте ещё раз.")
        else:
            print("Пожалуйста, выберите от 1 до 2.")

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
            diagonal = input("Введите диагональ экрана: ")
            dev = models.TV(typeofdevice, brand, diagonal, description)

        new_receipt = receipt.Receipt(dev, dateofreceive, dateofrepair, initials, status)
        self._listofreceipts.append(new_receipt)
