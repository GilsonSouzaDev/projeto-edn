def area(raio):
    PI = 3.14159
    area = PI * raio
    return area

def raio():
    raio = float(input("Insira o valor da raio: "))
    raio = round(raio, 2)
    raio = pow(raio, 2)
    return raio


print("A:", round(area(raio()),4))

