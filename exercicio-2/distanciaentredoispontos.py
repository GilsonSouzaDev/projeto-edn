import math

# Entrada dos dois pontos
ponto1 = input("Digite as coordenadas do primeiro ponto (x1 y1): ")
ponto2 = input("Digite as coordenadas do segundo ponto (x2 y2): ")

# Separação das coordenadas e conversão para ponto flutuante
x1, y1 = map(float, ponto1.split())
x2, y2 = map(float, ponto2.split())

# Cálculo da distância utilizando a fórmula
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Exibição do resultado
print(f"{distancia:.4f}")
