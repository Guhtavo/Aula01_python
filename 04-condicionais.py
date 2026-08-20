numero = int(input('Informe um numero: '))

resultado = int(numero % 2)
print('Se o resultado for  0 é par se for 1 é impar, o reaultado é: ', resultado)
input( 'Digite ENTER para continuar! ')

#if é usado para tomada de decisão
if resultado == 0:
    resultado ="O número é par"
else: resultado = "O número é impar"
print(resultado)
input('Digite ENTER para continuar')
