A = 0
B = 0
C = 0
D = 0

diferenca = 0

A = int(input("Digite o primeiro valor: "))
B = int(input("Digite o segundo valor: "))
C = int(input("Digite o terceiro valor: "))
D = int(input("Digite o quarto valor: "))

def dif(A, B, C, D):
    dif = 0
    dif = (A * B) - (C * D)
    return dif

diferenca = dif(A, B, C, D)

print(f"DIFERENCA = {diferenca} ")