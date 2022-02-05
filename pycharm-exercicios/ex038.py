n = int(input('\033[1;33mDigite o primeiro valor\033[m: '))
n1 = int(input('\033[1;33mDigite o segundo valor\033[m: '))
if n > n1 :
    print('\033[1;32mO primeiro valor é maior\033[m')
elif n < n1 :
    print('\033[1;32mO segundo valor é maior\033[m')
else:
    print('\033[1;31mNão existe valor maior, os dois são iguais.')