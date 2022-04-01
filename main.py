import models
import workshop
import receipt
import utils


def main():
    main_workshop = workshop.Workshop(utils.listOfReceipts)
    result_receipt = workshop.create_receipt()
    main_workshop.listofreceipts.append(result_receipt)
    main_workshop.print_receipts()


main()
