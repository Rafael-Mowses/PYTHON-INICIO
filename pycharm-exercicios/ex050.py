s = 0
ct = 0
for c in range(1, 7):
    n = int(input('Digite o {} valor: '.format(c)))
    if n % 2 == 0:
        s += n
        ct += 1
print('Você informou {} números PARES e a soma foi {}'.format(ct, s))