# I use this constant values to represent the user and the other account to transfer money
# In a real world situation, this values would be stored in a database
USERNAME = 'Ruben'
PASSWORD = '12345'
BALANCE = 2000
OTHER_USERNAME = 'Delas'
OTHER_ACCOUNT_NUMBER = 28940409

def main():
    print("#####################################")
    print("# Welcome to the Online Banking App #")
    print("#####################################\n")

    amount_of_tries = 3

    username = input("Please enter your username: ")

    while username != USERNAME:
        print("Invalid username")
        username = input("Please enter a valid username: ")

    password = input('Please enter your password: ')
    
    while password != PASSWORD:
        if amount_of_tries == 0:
            print("You have exceeded the number of tries")
            return
        
        print(f"Invalid password. Amount of tries left: {amount_of_tries}\n")
        amount_of_tries -= 1
        password = input("Please enter a valid password: ")

    balance = BALANCE

    print(f"You have successfully logged in.\n\nWelcome to the Online Banking App, {username}\n")
    print('type [deposit] to make a deposit\ntype [withdraw] to make a withdraw\ntype [balance] to check your balance\ntype [transfer] to make a transfer\ntype [logout] to logout\n')
    action = input('What would you like to do? ')

    # This is a very simple way to handle the user input
    while True:
        match action:
            case 'deposit':
                try: 
                    amount = int(input('Please enter the amount: '))
                    if amount <= 0:
                        print('Invalid amount\n')
                        continue
                    balance += amount
                    print(f'You have successfully deposited {amount}. Your new balance is {balance}\n')
                    action = input('[deposit|withdraw|balance|transfer|logout]')
                    continue
                except ValueError:
                    print('Invalid input\n')
                    continue

            case 'withdraw':
                try:
                    amount = int(input('Please enter the amount: '))
                    new_balance: int = withdraw(amount, balance)

                    if new_balance is not None:
                        balance = new_balance
                        print(f'Your new balance is: {new_balance}\n')
                        action = input('[deposit|withdraw|balance|transfer|logout]')
                        continue
                except ValueError:
                    print('Invalid input\n')
                    continue

            case 'balance':
                print(f'Your balance is: {balance}')
                action = input('[deposit|withdraw|balance|transfer|logout]')

            case 'transfer':
                try:
                    account = int(input('Please enter the account number: '))
                    amount = int(input('Please enter the amount: '))

                    new_balance: int = transfer(account, amount, balance)

                    if new_balance is not None:
                        balance = new_balance
                        print(f'Your new balance is: {new_balance}\n')
                        action = input('[deposit|withdraw|balance|transfer|logout]')
                        continue
                    
                    option = input('Want to try again? [y/n] ')

                    if option == 'y':
                        continue
                        
                    action = input('[deposit|withdraw|balance|transfer|logout]')
                except ValueError:
                    print('Invalid input\n')
                    continue

            case 'logout':
                print('You have successfully logged out. Cya later!')
                return
            
            case _:
                print('INVALIDAD ACTION')
                action = input('[deposit|withdraw|balance|transfer|logout]')

def transfer(account: int, amount: int, balance: int):
    if (account != OTHER_ACCOUNT_NUMBER):
        print('Invalid account number\n')
        return None
    
    if (amount > balance):
        print('Insufficient funds\n')
        return None
    
    if amount <= 0:
        print('Invalid amount\n')
        return None
    
    new_balance = balance - amount
    print(f'You have successfully transfered {amount} to {account}\n\n')
    return new_balance
    
def withdraw(amount: int, balance: int):
    if (amount > balance):
        print('Insufficient funds\n')
        return None

    if amount <= 0:
        print('Invalid amount\n')
        return None
    
    return balance - amount
    
if __name__ == '__main__':
    main()