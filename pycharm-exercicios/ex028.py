import random
from time import sleep
print('-=-'*20)
print('VOU PENSAR EM UM NÚMERO ENTRE 0 e 5. TENTE ADIVINHAR... ')
print('-=-'*20)
a = int(input('Em que número eu pensei: ')) # Jogador tenta adivinhar
print('PENSANDO...')
sleep(3)
n = random.randint(0,5) # Faz o computador "PENSAR"
if a == n :
    print('Parabéns, você conseguiu me vencer!. Vamos outra rodada! ')
else:
    print('Eu venci!, tente novamente ')
print('O número que eu pensei foi {}'.format(n))