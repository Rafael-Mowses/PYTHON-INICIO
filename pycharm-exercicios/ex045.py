import random
p = int(input('''Escolha uma opção para se jogar:

\033[1;33m[0] Pedra
[1] Papel
[2] Tesoura\033[m

Digite sua escolha: '''))
c = random.randint(0,2)
#computador escolheu 0(pedra)
if c == 0:
    print('O computador escolheu: \033[1;33mPedra\033[m')
    if p == 0:
        print('\033[1;34mEmpate\033[m!')
    elif p == 1:
        print('\033[1;32mVocê venceu\033[m!')
    elif p == 2:
        print('\033[1;31mComputador venceu\033[m!')
    else:
        print('Operação invalida')
#computador escolheu 1(papel)
elif c == 1:
    print('O computador escolheu: \033[1;33mPapel\033[m')
    if p == 0:
        print('\033[1;31mComputador venceu\033[m!')
    elif p == 1:
        print('\033[1;34mEmpate\033[m')
    elif p == 2:
        print('\033[1;32mVocê venceu\033[m!')
    else:
        print('Operação invalida')
#computador escolheu 2(tesoura)
elif c == 2:
    print('O computador escolheu: \033[1;33mTesoura\033[m')
    if p == 0:
        print('\033[1;32mVocê venceu\033[m!')
    elif p == 1:
        print('\033[1;31mComputador venceu\033[m!')
    elif p == 2:
        print('\033[1;34mEmpate\033[m')
    else:
        print('Operação invalida')
else:
    print('\033[1;31mOperação invalida')