valor1 = 0
valor2 = 0
resultadoFinal = 0

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

def prod (a, b):
    resultado = 0
    resultado = a * b
    return resultado

resultadoFinal = prod(valor1, valor2)

print("PROD =",resultadoFinal)
