n = int(input('Digite um número: '))
a = n * 2
a2 = n * 3
a3 = n ** (1/2)
print('O dobro de \033[1;31m{}\033[m é \033[1;32m{}\033[m.\ne o triplo de \033[1;31m{}\033[m é \033[1;32m{}\033[m,\ne a raiz quadrada de \033[1;31m{}\033[m é \033[1;33m{:.2f} ' .format(n, a, n, a2, n, a3))
