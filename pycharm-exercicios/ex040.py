n = float(input('Digite sua primeira nota: '))
n1 = float(input('Digite sua segunda nota: '))
a = (n + n1) / 2
if a < 5.0:
    print('\033[4;31mREPROVADO\033[m')
elif a == 5.0 or a < 6.9:
    print('\033[4;33mRECUPERAÇÃO\033[m')
elif a > 6.9:
    print('\033[1;32mAPROVADO\033[m')
print('Sua nota foi {}'.format(a))

