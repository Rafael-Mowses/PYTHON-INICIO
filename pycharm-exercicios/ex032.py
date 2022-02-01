a = int(input('Digite um ano: '))
if (a%4==0 and a%100!=0) or (a%400==0):
    print('\033[1;32m{} é um ano Bissexto\033[m'.format(a))
else:
    print('\033[1;312m{} não é um ano Bissexto'.format(a))
