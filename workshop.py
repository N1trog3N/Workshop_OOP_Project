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

    def admin_panel(self):
        print("\nПанель администратора")
        login = input("Введите логин: ")
        password = input("Введите пароль: ")

        if login in utils.ADMIN_DICT.keys() and utils.ADMIN_DICT.get(login)[0] == password:
            print("Авторизация прошла успешно.")
            while True:
                print("\nВыберите действие:")
                print("\nДействия с администраторами:")
                print("  1. Просмотреть список администраторов")
                print("  2. Удаление администратора")
                print("  3. Добавить нового администратора")
                print("\nДействия с квитанциями:")
                print("  4. Изменить статус ремонта")
                print("  5. Изменить дату выполнения ремонта")
                print("  6. Просмотреть информацию о квитанции")

                print("\n7. Выход")
                sw = int(input())

                if sw == 1:
                    self.view_list_of_admins()

                elif sw == 2:
                    self.remove_admin()

                elif sw == 3:
                    self.add_admin()

                elif sw == 4:
                    self.change_repairing_status()

                elif sw == 5:
                    self.change_date_of_repair()

                elif sw == 6:
                    self.receipts_admin_info()

                elif sw == 7:
                    break

        else:
            print("Неверные данные для входа. Попробуйте еще раз.")

    @staticmethod
    def view_list_of_admins():
        count = 1
        for i, j in utils.ADMIN_DICT.items():
            print(f"{count}. Логин: {i}, Пароль: {j[0]}, ФИО: {j[1]}")
            count += 1

    @staticmethod
    def remove_admin():
        count = 1
        for i, j in utils.ADMIN_DICT.items():
            print(f"{count}. Логин: {i}, Пароль: {j[0]}, ФИО: {j[1]}")
            count += 1
        num = int(input("Введите номер администратора для удаления:"))
        utils.ADMIN_DICT.pop(list(utils.ADMIN_DICT.keys())[num - 1])

    @staticmethod
    def add_admin():
        login = input("Введите новый логин: ")
        password = input("Введите новый пароль: ")
        initials = input("Введите ФИО: ")
        utils.ADMIN_DICT[login] = [password, initials]

    def change_repairing_status(self):
        print("\nИзменение статуса ремонта")
        found = False
        num = int(input("Введите номер квитанции: "))
        for i in self._listofreceipts:
            if i._number == num:
                status = int(input("Выберите новый статус: \n1. Ремонтируется  \n2. Готов к выдаче  \n3. Выдан клиенту\n"))
                i._status = utils.LIST_OF_STATUSES[status - 1]
                found = True
        if not found:
            print("Квитанция с таким номером не найдена.")

    def change_date_of_repair(self):
        print("\nИзменение даты выполнения ремонта")
        found = False
        num = int(input("Введите номер квитанции: "))
        for i in self._listofreceipts:
            if i._number == num:
                new_date = input("Введите дату: ")
                i._dateOfRepair = new_date
                found = True
        if not found:
            print("Квитанция с таким номером не найдена.")

    def receipts_admin_info(self):
        print("\nЧтобы просмотреть информацию о квитанциях, введите номер квитанции или ФИО клиента:")
        print("1. Ввести ФИО клиента")
        print("2. Ввести номер квитанции")
        sw = int(input())

        if sw == 1:
            info = input("Введите ФИО клиента: ")
            found = False
            for i in self._listofreceipts:
                if i._initials == info:
                    found = True
                    print(i)

            if not found:
                print("Квитанций на данного клиента не найдено. Попробуйте ещё раз.")

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
