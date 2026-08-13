#calculos
num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

soma = int(num1) + int(num2)

subtracao = int(num1) - int(num2)
divisao = int(num1) / int(num2)
moduloresto = int(num1) % int(num2)
multiplicacao = int(num1) * int(num2)
potencia = int(num1) * int(num2)


print("Resultado da soma: ", soma)
print("Resultado da subtracao: ", subtracao)
print("Resultado da divisao: ", divisao)
print("Resultado da moduloresto: " ,moduloresto)
print("Resultado da multiplicacao: ", multiplicacao)
print("Resultado da potencia: ", potencia)

#O comando type retorna o tipo da variavel.
print(type(num1))
print(type(soma))

#calcular aréa
lado1 = input("Informe o primeiro lado: ")
lado2 = input('Informe o segundo lado: ')

area = float(lado1) + float(lado2)

print("A area do quadrado é: {}" .format(area))

nomecompleto = input('Informe p seu nome completo: ')
#funão len retorno a quantidade de caracteres de uma varavel

print('1. Quantidade de caracteres: ', len(nomecompleto))

#upper = trasforma um texto em maiusculo
#lower = transforma um texto em minusculo
#capitalize = somente a primeira letra em maiusculo
print('2. Nome em maiusculo: ', nomecompleto.upper)
print('3. Nome em maiusculo: ', nomecompleto.lower())
print('4. Primeira letra em maiusculo: ', nomecompleto.capitalize())

