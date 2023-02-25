print("combinação de  numeros 3 a 3")
lista = [0] * 5
x1 = x2 = x3 = ac_qtde = 0
while x1 < 55:
  lista[x1] = int(input("Digite um numero: "))
  x1 = x1 + 1
x1 = 0 
for x1 in range (0,3): 
    for x2 in range (x1 + 1,):
      for x3 in range (x2, 1,5):
        print (lista[x1],"",lista[x2],"",lista[x3])
        ac_qtde = ac_qtde + 1
print("qtde de combinações = ", ac_qtde)
a = input("pressione enter para sair")