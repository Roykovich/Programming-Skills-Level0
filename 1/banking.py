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
                    # First we ask for the amount, it should be an integer or it will raise a ValueError
                    amount = int(input('Please enter the amount: '))
                    # Then we check if the amount is greater or equal to 0
                    if amount <= 0:
                        print('Invalid amount\n')
                        continue
                    # If the amount is valid, we add it to the balance and print the new balance
                    balance += amount
                    print(f'You have successfully deposited {amount}. Your new balance is {balance}\n')
                    # Finally we ask the user what he wants to do next
                    action = input('[deposit|withdraw|balance|transfer|logout]')
                    continue
                except ValueError:
                    print('Invalid input\n')
                    continue

            case 'withdraw':
                try:
                    # First we ask for the amount, it should be an integer or it will raise a ValueError
                    amount = int(input('Please enter the amount: '))
                    # Then we call the withdraw function, it will return the new balance or None if the amount is invalid
                    new_balance: int = withdraw(amount, balance)
                    # If the amount is valid we update the balance and print the new balance
                    if new_balance is not None:
                        balance = new_balance
                        print(f'Your new balance is: {new_balance}\n')
                        # Finally we ask the user what he wants to do next
                        action = input('[deposit|withdraw|balance|transfer|logout]')
                        continue
                except ValueError:
                    print('Invalid input\n')
                    continue

            case 'balance':
                # We just print the balance and ask the user what he wants to do next
                print(f'Your balance is: {balance}')
                action = input('[deposit|withdraw|balance|transfer|logout]')

            case 'transfer':
                try:
                    # First we ask for the account number and the amount, they should be integers or it will raise a ValueError
                    account = int(input('Please enter the account number: '))
                    amount = int(input('Please enter the amount: '))

                    # Then we call the transfer function, it will return the new balance or None if the account or the amount are invalid
                    new_balance: int = transfer(account, amount, balance)

                    # If the amount is valid we update the balance and print the new balance
                    if new_balance is not None:
                        balance = new_balance
                        print(f'Your new balance is: {new_balance}\n')
                        # Finally we ask the user what he wants to do next
                        action = input('[deposit|withdraw|balance|transfer|logout]')
                        continue
                    
                    # If the account or the amount are invalid, we ask the user if he wants to try again
                    option = input('Want to try again? [y/n] ')

                    # If the user wants to try again, we continue the loop
                    # and ask for the account and the amount again
                    if option == 'y':
                        continue
                    
                    # If the user doesn't want to try again, we ask the user what he wants to do next
                    action = input('[deposit|withdraw|balance|transfer|logout]')
                except ValueError:
                    print('Invalid input\n')
                    continue

            case 'logout':
                # We just print a message and end the program
                print('You have successfully logged out. Cya later!')
                return
            
            case _:
                # If the user types an invalid action, we ask the user what he wants to do next
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