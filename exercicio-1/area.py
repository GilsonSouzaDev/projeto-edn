PI = 3.14159
raio = 0.0
areaFinal = 0.0

def area(pi, raio):
    area = 0.0
    area = pi * raio
    return area

raio = float(input("Insira o valor da raio: "))

raio = round(raio, 2)

raio = pow(raio, 2)

print("A:", round(area(PI, raio),4))

