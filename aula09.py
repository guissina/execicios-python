#frase = 'Curso em Video Python'
#print(len(frase))
#print(frase.count('o'))
#print(frase.find('urso'))
#if 'Curso' in frase:
#    frase = frase.replace('Python','Android')
#    frase = frase.lower()
#else:
#    frase = frase.replace('Pyhton', 'Apple')
#print(frase)

#frase = input('Digite uma frase: ')
#frase = frase.strip()
#print('a frase tem ', len(frase), ' caracteres')
#frase = frase + ' taokey?'
#print(frase)

#nome = input('Digite um nome completo: ')
#print('todas maiusculas:', nome.upper())
#print('todas minusculas:', nome.lower())
#print('tamanho c espacos:', len(nome))
#nome = nome.split()
#print('tamanho do primeiro nome:', len(nome[0]))
#nome = ''.join(nome)
#print(''.join(nome.split()))
#print(nome)
#print('tamanho sem espacos:', len(nome))

#x = int(input('Digite um numero de 0 a 9999: '))
#u = x // 1 % 10
#d = x // 10 % 10
#c = x // 100 % 10
#m = x // 1000 % 10
#print('Unidade: {}'.format(u))
#print('Dezena: {}'.format(d))
#print('Centena: {}'.format(c))
#print('Milhar: {}'.format(m))

#mesmo programa em string
num = int(input('Digite um numero de 0 a 9999: '))
num = str(num)
u = 0
d = 0
c = 0
m = 0
if len(num) != 4:
    if len(num) != 3:
        if len(num) != 2:
            if len(num) < 5:
                u = num[0]
            else:
                print('Numero invalido')
        else:
            u = num[1]
            d = num[0]
    else:
        u = num[2]
        d = num[1]
        c = num[0]
else:
    u = num[3]
    d = num[2]
    c = num[1]
    m = num[0]
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
