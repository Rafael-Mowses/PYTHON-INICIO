v = float(input('Digite qual foi a velocidade: '))
if v > 80:
    print('\033[31mVocê excedeu o limite permitido que é de 80Km/h\033[m')
    m = (v-80) * 7
    print('\033[31mVocê deve pagar uma multa de R${:.2f}\033[m'.format(m))
    print('\033[1;31mDirija com segurança seu otario tá colocando a sua vida e de outras pessoas em risco.\033[m')
else:
    print('\033[1;32mVocê não excedeu o limite!, Parabens!!')


