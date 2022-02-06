from datetime import date
a = date.today().year
t = 0
t1 = 0
for p in range(1, 8):
    n = int(input('Em que ano a {}ª pessoa nasceu? '.format(p)))
    i = a - n
    if i >= 21:
        t += 1
    else:
        t1 += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(t))
print('E também tivemos {} pessoas menores  de idade'.format(t1))