import random

letters_lower = 'abcdefghijklmnopqrstuvwxyz'
letters_upper = 'ABCDEJGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
symbols_basic = '!?#$&*@'
symbols_extra = '%()+-=[]{}|~.,'

def pwgen(size=0, lower=0, upper=0, nums=0, sym1=0, sym2=0):
    chars = ''
    pw = ''
    if lower == 1:
        chars += letters_lower
    if upper == 1:
        chars += letters_upper
    if nums == 1:
        chars += digits
    if sym1 == 1:
        chars += symbols_basic
    if sym2 == 1:
        chars += symbols_extra
    for i in range(size):
        pw += random.choice(chars)
    return pw

while True:
    try:
        size = int(input('Length of password?\n'))
        break
    except ValueError:
        print('Enter an integer')

while True:
    try:
        howmany = int(input('How many?\n'))
        break
    except ValueError:
        print('Enter an integer')

while True:
    lower = input('Use lowercase letters? (abcdefghijklmnopqrstuvwxyz)\n')
    if lower.lower() == 'y':
        lower = 1
        break
    elif lower.lower() == 'n':
        lower = 0
        break
    else:
        print('Enter Y or N')

while True:
    upper = input('Use uppercase letters? (ABCDEJGHIJKLMNOPQRSTUVWXYZ)\n')
    if upper.lower() == 'y':
        upper = 1
        break
    elif upper.lower() == 'n':
        upper = 0
        break
    else:
        print('Enter Y or N')

while True:
    nums = input('Use digits? (0123456789)\n')
    if nums.lower() == 'y':
        nums = 1
        break
    elif nums.lower() == 'n':
        nums = 0
        break
    else:
        print('Enter Y or N')

while True:
    sym1 = input('Use basic symbols? (!?#$&*@)\n')
    if sym1.lower() == 'y':
        sym1 = 1
        break
    elif sym1.lower() == 'n':
        sym1 = 0
        break
    else:
        print('Enter Y or N')

while True:
    sym2 = input('Use more symbols? (%()+-=[]{}|~.,)\n')
    if sym2.lower() == 'y':
        sym2 = 1
        break
    elif sym2.lower() == 'n':
        sym2 = 0
        break
    else:
        print('Enter Y or N')

for i in range(howmany):
    print(pwgen(size, lower, upper, nums, sym1, sym2))
