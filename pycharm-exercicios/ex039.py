from datetime import date
a = date.today().year
n = int(input('Ano de nascimento: '))
i = a - n
print('Quem nasceu em {} tem {} anos em {}.'.format(n, i, a))
if i == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif i < 18:
    s = 18 - i
    print('Ainda faltam {} anos para o alistamento'.format(s))
    ano = a + s
    print('Seu alistamento será em {}.'.format(ano))
elif i > 18:
    s = i - 18
    print('Você já deveria ter se alistado há {} anos.'.format(s))
    ano = a - s
    print('Seu alistamento foi em {}'.format(ano))