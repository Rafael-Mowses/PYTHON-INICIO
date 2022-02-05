c = float(input('Valor da casa: R$'))
s = float(input('Salário do comprador: R$'))
a = int(input('Quantos anos de financiamento: '))
p = c / (a * 12)
m = s * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(c, a), end='')
print(' a prestação de R${:.2f}'.format(p))
if p <= m:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')