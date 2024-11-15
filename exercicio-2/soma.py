valor1 = 0
valor2 = 0
resultadoFinal = 0

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

def soma (a, b):
    resultado = 0
    resultado = a + b
    return resultado

resultadoFinal = soma(valor1, valor2)

print("X =",resultadoFinal)


