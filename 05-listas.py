frutas = ["maçã", "banana", "uva"]
print(frutas)

print(frutas[1])
print(frutas[2])

#Modificando
frutas[1] = "laranja"
print(frutas)

#adicionando itens no fial da lista
frutas.append("pera")
print(frutas)

#adicionando no começo da lista
frutas.insert(0, "abacaxi")
print (frutas)
# procurando 
indice = frutas.index("uva")
print(indice) 

if "uva" in frutas:
 print ("Uva esta na lista")

 #Removendo itens
 frutas.remove("uva")
 print(frutas)

 #removendo
 if "uva" in frutas:
   print("uva esta na lista!")
else:
  print("uva foi removida")

#tamanho da lista
numeros = [100, 28, 4, 31, 25]
print(len(numeros))

#ordenar
numeros.sort()
print(numeros)

frutas.sort()
print(frutas)

#inverter
numeros.reverse()
print(numeros)

frutas.reverse()
print(frutas)

#verificar se existe na lista de numeros
print(2 in numeros)
print(100 in numeros)

#adicionando varios elementos 
numeros =[10,20,30] + numeros

#ordenei
numeros.sort()
print(numeros)

#percorrendo uma lista com laço for

for n in numeros:
  print(n)
  print(type(n))
  print(numeros)