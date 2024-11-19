#Declarando inicializando variaveis de entrada
A = 0
B = 0
C = 0
D = 0

# Declarando e inicializando variavel de saida
diferenca = 0

# Coletando valores de entrada do usuario
A = int(input("Digite o primeiro valor: "))
B = int(input("Digite o segundo valor: "))
C = int(input("Digite o terceiro valor: "))
D = int(input("Digite o quarto valor: "))

# funcao para realizar o calculo da diferença
def dif(A, B, C, D):
    dif = 0
    dif = (A * B) - (C * D)
    return dif

# Chamando a funcao para realizar o calculo e atribuindo a variavel de saida
diferenca = dif(A, B, C, D)

# Imprimando a mensagem e valor de saida
print(f"DIFERENCA = {diferenca} ")