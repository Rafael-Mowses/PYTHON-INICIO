n = int(input('Digite um valor em metros: '))
a1 = n * 0.001
a2 = n * 0.01
a3 = n * 0.1
a4 = n * 10
a5 = n * 100
a6 = n * 1000
print('A medida de {} corresponde a'.format(n))
print('{}km\n{}hm\n{:.1f}dam\n{}dm\n{}cm\n{}mm'.format(a1, a2, a3, a4, a5, a6))
