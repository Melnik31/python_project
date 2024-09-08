def menu():
    print('\nMenu:')
    print('\n1. Add transaction')
    print('2. View transactions')
    print('3. Delete transaction')
    print('4. Exit')

def add_trans(transactions):
    print('\nEnter "0" to exit')
    while True:
        amount = input('Enter the amount: ')
        if amount == '0':
            break
        transactions.append(int(amount))
    
def view_transactions(transactions):
    print('\nAll transactions: ')

    for i, transaction in enumerate(transactions, 1):
        print(f'{i}. ${transaction}')
    print(f'\nTotal: ${sum(transactions)}')

def delete(transactions):
    if not transactions:
        print('No transatcions added yet.')
        return
    
    view_transactions(transactions)

    user_pick = int(input('Enter the transaction number: ')) - 1
    if 0 <= user_pick < len(transactions):
        delete_trans = transactions.pop(user_pick)
        print(f'Transaction {delete_trans} was deleted.')
    else:
        print('Transaction number do not match.')

def main():
    transactions = []

    while True:

        menu()

        choice = input("Enter the number to use a menu: ")
        
        if choice == '1':
            add_trans(transactions)
        elif choice == '2':
            view_transactions(transactions)
        elif choice == '3':
            delete(transactions)
        elif choice == '4':
            print('Exiting...')
            break
        else:
            print('Invalid input')

main()
