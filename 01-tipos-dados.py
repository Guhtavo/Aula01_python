''' comentrios: auxiliam a deixar 
"anotações" no codigo fonte'''

#Contatenação.
print('Boas vindas a aula de ' + "Python!")

#Interpulação
print('Olá, {}' . format(input('Digite seu nome: ')))


#Tipos de dados em python - numeros

#Interiros
idade = 25
print(idade)

#Decimal (float)
altura = 1.75
print(altura)

#Texto complexo
numero_complexo = 2 + 3j
print(numero_complexo)

#texto(str)
nome = "Gustavo Antonio"
print(nome)


#Boleanos
ativo = True
print(ativo)

logado = False
print(logado)

#nenhum valor (NoneType)
valor = None
print(valor)


#Lista (list) mutavel
frutas = ["maçã", "banana", "uva"]
print(frutas)

#tuplas(tuple set) imutavel
cores = ("vernmelho", "azul", "verde")
print(cores)

#conjuto
numeros = {1, 2, 3, 4}
print(numeros)

#Dicionario (dict) pares chave-valor
pessoas = {
    "nome":"Gustavo",
    "idade": 30
}
print(pessoas)


''' python não tem constantes
verdadeiras, mas usamos uma convenção
para indiar que um valor não deve ser alterado'''
PI = 3.14159

GRAVIDADE = 9.8

print("O valor de PI é ", PI, "\nO valor de Gavidade é " , GRAVIDADE)