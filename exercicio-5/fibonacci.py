def calculofibonacci(n):
    a, b = 0, 1
    resultado = [a]
    for i in range(1, n):
        resultado.append(b)
        a, b = b, a + b
    return resultado

def main():
    try:
        N = int(input("Digite um valor inteiro para N: "))
        if N < 1 or N > 46:
            raise ValueError("O valor de N deve estar entre 1 e 46")
        sequencia = calculofibonacci(N)
        print("Serie de fibonacci: ", sequencia)
    except ValueError as ve:
        print(f"erro: {ve}")
main()
