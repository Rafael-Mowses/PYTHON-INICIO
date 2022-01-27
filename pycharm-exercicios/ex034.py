s = float(input('Informe seu salario: R$'))
a = s * 1.10
a1 = s * 1.15
if s >=1250:
    print('Seu salário com aumento de 10% R${:.2f}'.format(a))
else:
    print('Seu salário com aumento de 15% R${:.2f}'.format(a1))