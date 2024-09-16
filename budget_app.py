import db
from datetime import datetime

#db.add_one("Place", 99)

#db.delete_one('5')

'''record = [
    ("Restoran", 51),
    ("Shop", 12),
    ("Other", 89),
]
'''
#db.add_many(record)

def menu():
    print('\nMenu:')
    print('\n1. Add transaction')
    print('2. View transactions')
    print('3. Delete transaction')
    print('4. Exit')

def add_trans():
    print('\nEnter "0" to exit')
    while True:
        name = input('Enter the store or transaction name: ')
        amount = input('Enter the amount: ')
        date = datetime.now().strftime('%m-%d-%Y')
        if amount == '0':
            break
        db.add_one(name,amount,date)

def view_transactions():
    print('\nAll transactions: ')

    db.show_all()


def delete():
    transactions = db.show_all()  # Ensure show_all() returns the transactions with rowid
    existing_ids = [trans[0] for trans in transactions]  # Extract rowid values
    
    while True:
        id_input = input('Enter the ID of transaction you want to delete.(Enter 0 to stop):')
        if id_input == '0':
            break
        try:
            id_input = int(id_input)
            if id_input in existing_ids:
                db.delete_one(id_input) 
                print(f'Transaction with ID({id_input}) was deleted.')
            else:
                print('Invalid ID. ID does not exist')
        except ValueError:
            print('Invalid input. Enter the number.')
    


def main():

    while True:

        menu()

        choice = input("Enter the number to use a menu: ")
        
        if choice == '1':
            add_trans()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            delete()
        elif choice == '4':
            print('Exiting...')
            break
        else:
            print('Invalid input')


if __name__ == "__main__":
    main()