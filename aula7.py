#n = int(input("digite um numero: "))
#b = n-1
#m = n+1
#print("{} o antecessor e {} o sucessor de {}".format(b,m,n))


#n1 = float(input("digite a primeira nota: "))
#n2 = float(input("digite a segunda nota: "))
#m = (n1 + n2)/2
#print("sua media é: {}".format(m))


#n = float(input("digite um valor em metros: "))
#cent = n*100
#mil = n*1000
#print("o valor em centimetros é {:>.0f} e em milimetros é {:>.0f}".format(cent,mil))


n = int(input("digite um numero: "))
controle = 0
r = 0
while controle != 10:
  r = n * controle
  print("{} x {} = {}".format(n,controle,r))
  controle = controle+1
a = input("press ENTER to exit")