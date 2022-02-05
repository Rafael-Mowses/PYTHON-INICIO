from datetime import date
a = date.today().year
n = int(input('Ano de Nascimento: '))
i = a - n
print('O atleta tem {} ano.'.format(i))
if i <= 9:
    print('Classificação: MIRIM')
elif i <= 14:
    print('Classificação: INFANTIL')
elif i <= 19:
    print('Classificação: JUNIOR')
elif i <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')