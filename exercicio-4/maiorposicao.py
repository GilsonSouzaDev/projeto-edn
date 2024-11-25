numeros = []
while len(numeros) < 5:
    numeros.append(int(input("Digite um número: ")))

num = 0  
posicao = 0       

for i in range(len(numeros)):
    if numeros[i] > num:  
        num = numeros[i]
        posicao = i + 1

print("Maior número:", num)
print("Posição do maior número:", posicao)