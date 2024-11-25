def main():
    try:
        X = int(input())
        Y = int(input())
        
        if X > Y:
            X, Y = Y, X

        print("--")

        for i in range (X + 1, Y):
            if i % 5 == 2 or i % 5 == 3:
                print(i)
        
        
    except ValueError:
        print("Erro: entrada invalida. Insira números inteiros!")

main()            