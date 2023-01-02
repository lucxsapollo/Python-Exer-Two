print('Perguntas para o exercito')

idade = int(input('Qual sua idade? '))
peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))

if idade >= 18 and peso >= 60 and altura >= 1.70:
    print('Você entrou para o exercito')
else:
    print('Você não entrou para o exercito')
