for num in range(1, 101):
    if num % 15 == 0:
        print('Fizz Buzz', end=',')
    elif num % 5 == 0:
        print('Buzz', end=',')
    elif num % 3 == 0:
        print('Fizz', end=',')
    else:
        print(num, end=',')

print()

for num in range(1, 101):
    mess = ''
    if num % 3 == 0:
        mess += 'Fizz'
    if num % 5 == 0:
        mess += 'Buzz'

    print(mess or num, end=',')
