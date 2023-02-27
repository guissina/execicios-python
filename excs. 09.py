#nome = input("digite um nome completo: ")
#nome = nome.split()
#print(nome[0])
#print(nome[-1])

#procura silva no nome
#nome = str(input('digite um nome: ')).strip()
#print('Analisando seu nome...')
#print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))

#procura 'Santo'
cidade = str(input("Digite uma cidade: ")).strip()
print('Essa cidade tem Santo no nome? {}'.format('santo' in cidade.lower()))
cidade = cidade.lower()
cidade = cidade.split()
print('Tem Santo no primeiro nome? {}'.format('santo' in cidade[0]))
