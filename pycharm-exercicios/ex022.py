nome = input('\033[1;33mDigite seu nome completo: ')
a = nome.upper()
a1 = nome.lower()
a2 = nome.replace(" ", "")
a3 = len(a2)
a4 = nome.split()
aa = (a4[0])
a6 = len(aa)
print('Seu nome com todas as letras maiúsculas \n{}'.format(a))
print('Seu nome com todas as letras minúsculas \n{}'.format(a1))
print('Seu nome tem {} letras'.format(a3))
print('Seu primeiro nome tem {} letras'.format(a6))

