v = float(input('Digite qual foi a velocidade: '))
if v > 80:
    print('Você excedeu o limite permitido que é de 80Km/h')
    m = (v-80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(m))
    print('Dirija com segurança seu otario tá colocando a sua vida e de outras pessoas em risco.')
else:
    print('Você não excedeu o limite!, Parabens!!')


