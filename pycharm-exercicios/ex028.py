import random
from time import sleep
print('-=-'*20)
print('VOU PENSAR EM UM NÚMERO ENTRE 0 e 5. TENTE ADIVINHAR... ')
print('-=-'*20)
a = int(input('\033[1;31;107mEm que número eu pensei\033[m: ')) # Jogador tenta adivinhar
print('\033[1;33mPENSANDO...\033[m')
sleep(3)
n = random.randint(0,5) # Faz o computador "PENSAR"
if a == n :
    print('\033[4;32mParabéns, você conseguiu me vencer!. Vamos outra rodada!\033[m ')
else:
    print('\033[1;31mEu venci!, tente novamente\033[m ')
print('O número que eu pensei foi \033[1;32m{}'.format(n))