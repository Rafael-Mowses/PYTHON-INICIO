print('\033[1;32m1 para binário\n2 para octal\n3 para hexadecimal\033[m')
n = int(input('Digite qual será a base de conversão: '))
n1 = int(input('Digite qual número será convertido: '))
b = bin(n1)[2:]
b1 = oct(n1)[2:]
b2 = hex(n1)[2:]
if n == 1 :
    print('Esse número {} convertido para binário é \033[1;32m{}\033[m '.format(n1, b))
elif n == 2 :
    print('Esse número {} convertido para octal é \033[1;32m{}\033[m'.format(n1, b1))
elif n == 3 :
    print('Esse número {} convertido para hexadecimal é \033[1;32m{}\033[m '.format(n1, b2))
else:
    print('Opção inválida. Tente novamente.')
