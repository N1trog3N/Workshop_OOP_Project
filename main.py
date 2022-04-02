import workshop
import utils

main_workshop = workshop.Workshop(utils.LIST_OF_RECEIPTS)
main_workshop.create_receipt()
result_receipt = main_workshop.print_receipts()
print(result_receipt[0])
