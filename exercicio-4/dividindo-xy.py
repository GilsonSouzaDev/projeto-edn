def main():
    n = int(input("Digite o numero de pares de valores: "))
    if n < 1:
        raise ValueError("Numero de pares - valores (N) deve ser maior que zero")
    for _ in range(n):
        try:
            x, y = map(int, input("Digeite os valores de X e Y separados por espaço: ").split())
            if y == 0:
                print("Divisão impossivel")
            else:
                resultado = x / y
                print(f"{resultado:.1f}")
        except ValueError:
            print("Erro: Certifique-se de inserir 2 números inteiros separados por espaço")

        except ValueError as ve:
            print(f"Erro: {ve}")

main()            