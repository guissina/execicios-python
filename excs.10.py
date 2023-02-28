import random

#print('Jogo de adivinha, tente acertar o numero pensado pelo computador')
#num = int(input('Digite um numero: '))
#x1 = 0
#lista = [0] * 100
#while x1 < 100:
#    lista[x1] = [x1 * 1]
#    x1 = x1 + 1
#rand = random.choice(lista)
#print('Valor pensado: {}'.format(rand))

#mesmo programa com 'if'
#print('Jogo de adivinha, tente acertar o numero pensado pelo computador')
#num = int(input('Digite seu chute (numero de 0 a 5): '))
#rand = random.randint(0, 5)
#if num == rand:
#    print('O valor chutado ({}) e o valor pensado pelo computador ({}) foram os mesmos, parabens!'.format(num, rand))
#else:
#    print('O valor chutado ({}) e o valor pensado pelo computador ({}) foram diferentes, que pena!'.format(num, rand))
#print('---Fim do Programa---')

#programa determina valor multa
#print('Programa determina o valor da sua multa')
#vel = int(input('Digite a velocidade: '))
#if vel > 80:
#    valor = (vel-80) * 7
#    print('O valor da multa foi de R${:.2f}'.format(valor))
#else:
#    print('Nao houve trangressao as leis do transito, sem multa')

#programa mostra se numero e par ou impar
#numero = int(input('Digite um numero a ser verificado: '))
#if numero % 2 == 0:
#    print('O numero {} e par'.format(numero))
#else:
#    print('O numero {} e impar'.format(numero))

#programa calcula custo viagem
dist = float(input('Digite a distancia da viagem: '))
if dist <= 200:
    valor = dist * 0.5
else:
    valor = dist * 0.45
print('O valor da viagem com {:.0f}km e de R${:.2f}'.format(dist, valor))