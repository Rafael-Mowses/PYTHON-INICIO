n = float(input('Quantos dias alugados: '))
n1 = float(input('Quantos Km rodados: '))
a = n * 60
a1 = n1 * 0.15
a2 = a + a1
print('O total a pagar é de R${:.2f}'.format(a2))
