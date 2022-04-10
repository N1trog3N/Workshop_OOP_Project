import workshop
import utils

main_workshop = workshop.Workshop(utils.LIST_OF_RECEIPTS)


def menu():
    print("\nВыберите действие:")
    print("1. Сдать технику в ремонт")
    print("2. Просмореть информацию о квитанциях")
    print("3. Выход")

    sw = int(input())

    if sw == 1:
        main_workshop.create_receipt()
    elif sw == 2:
        main_workshop.print_receipts()
    elif sw == 3:
        quit()
    else:
        print("Пожалуйста, выберите от 1 до 3.")


while True:
    menu()
