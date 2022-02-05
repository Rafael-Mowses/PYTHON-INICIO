p = float(input('Informe seu peso (kg): '))
a = float(input('Informe a sua altura (metro e cm): '))
i = p / (a * a)
if i < 18.5:
    print('Abaixo do peso')
elif i == 18.5 or i < 25:
    print('Peso ideal')
elif i == 25 or i < 30:
    print('Sobrepeso')
elif i == 30 or i < 40:
    print('Obesidade')
elif i > 40:
    print('Obesidade mórbida')