n1 = float(input('\033[1;34mQual o valor do produto\033[m: R$'))
print('\033[1;33m[ 1 ] para à vista\n[ 2 ] à vista no cartão\n[ 3 ] em até 2x no cartão\n[ 4 ] 3x ou mais no cartão\033[m')
n = int(input('\033[1;34mQual vai ser a forma de pagamento\033[m: '))
a = n1 * 0.9
a1 = n1 * 0.95
a2 = n1 * 1.20
if n == 1:
    print('\033[1;32mCom 10% de desconto você pagará\033[m R${:.2f}'.format(a))
elif n == 2:
    print('\033[1;32mCom 5% de desconto você pagará\033[m R${:.2f}'.format(a1))
elif n == 3:
    print('\033[1;32mVocê pagará o valor normal de\033[m R${:.2f}'.format(n1))
elif n == 4:
    print('\033[1;32mCom 20% de juros você pagará\033[m R${:.2f}'.format(a2))
print('\033[1;35mVOLTE SEMPRE!!')
