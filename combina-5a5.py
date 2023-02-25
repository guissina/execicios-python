print ("combinacao de 8 numeros 5 a 5")
lista=[0] * 8
x1 = x2 = x3 = x4 = x5 = 0      #Números a serem combinados
### obter numeros a combinar ###
while x1 < 8 :
    lista [x1] = int(input("Digite um numero: "))
    x1 = x1 + 1
#
# combina 8 números 5 a 5
x1 = 0
contador = 0      #contador de combinações"
for  x1 in  range (0, 4) :
    for  x2  in  range (x1 + 1, 5) :
        for  x3  in  range (x2 + 1, 6)  :
             for  x4  in  range (x3 + 1, 7) :
                 for  x5  in  range (x4 + 1, 8)  :
                    print(lista [x1], " ",lista [x2], " ",lista [x3], " ",lista [x4], " ",lista [x5])
                    contador = contador + 1
print ("Quantidade de combinacoes feitas = ",contador)
a= input ("Pressione enter para sair")
