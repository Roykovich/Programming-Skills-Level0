CURRENCY = {
    'USD': {
        'EUR': 0.92,
        'ARS': 810.64,
        'CLP': 882.23,
        'TRY': 29.79,
        'GBP': 0.79,
    },
    'EUR': {
        'USD': 1.09,
        'ARS': 885.80,
        'CLP': 964,
        'TRY': 32.55,
        'GBP': 0.86,
    },
    'ARS': {
        'USD': 0.0012,
        'EUR': 0.0011,
        'CLP': 1.09,
        'TRY': 0.037,
        'GBP': 0.00097,
    },
    'CLP': {
        'USD': 0.0011,
        'EUR': 0.0010,
        'ARS': 0.92,
        'TRY': 0.034,
        'GBP': 0.00089,
    },
    'TRY': {
        'USD': 0.034,
        'EUR': 0.031,
        'ARS': 27.21,
        'CLP': 29.62,
        'GBP': 0.026,
    },
    'GBP': {
        'USD': 1.27,
        'EUR': 1.16,
        'ARS': 1027.35,
        'CLP': 1118.06,
        'TRY': 37.75,
    }
}

def main():
    print('######################################')
    print('# Welcome to the currency converter! #')
    print('######################################\n\n')

    print('Available currencies: [USD|EUR|ARS|CLP|TRY|GBP]')
    from_currency = input('Initial currency: ').upper()
    to_currency = input('Final currency: ').upper()
    print(f'\n{from_currency}: 1   ===>   {CURRENCY[from_currency][to_currency]}\n\n')
    action = input('What you want to do? [W]ithdraw, [T]able or [Q]uit: ').upper()

    while True:
        match action:
            case 'W':
                try: 
                    # First we ask for the amount, it should be an integer or it will raise a ValueError
                    amount = int(input('Please enter the amount: '))
                    # Then we check if the amount is greater or equal to 0
                    if amount <= 0:
                        print('Amount should be greater that 0 \n')
                        continue

                    total = amount * CURRENCY[from_currency][to_currency]

                    print(f'\n{amount} {from_currency} ===> {total} {to_currency} - 1% comission = [{total * 0.99} {to_currency}]\n')
                    

                    action = input('What you want to do? [W]ithdraw, [T]able or [Q]uit: ').upper()
                    continue
                except ValueError:
                    print('Invalid input\n')
                    continue
            case 'T':
                for currency, value in CURRENCY[from_currency].items():
                    print(f'{currency}: {value}')
                action = input('What you want to do? [W]ithdraw, [T]able or [Q]uit: ').upper()
                continue
            case 'Q':
                print('Bye!')
                return
            case _:
                print('Invalid input\n')
                action = input('[W]ithdraw, [T]able or [Q]uit: ').upper()
                continue
    
if __name__ == '__main__':
    main()