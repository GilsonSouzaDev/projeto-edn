nomeVendedor = " ";
totalDeVendaMes = 0.0
valorSalarioFixo = 0.0

salarioVendedor = 0.0

while True:

    print("\n------------------------------------------------")
    nomeVendedor = input("Digite o nome do vendedor: ")
    valorSalarioFixo = float(input("Digite o valor do salario do vendedor: "))
    totalDeVendaMes = float(input("Digite o total de vendas realizada (Em dinheiro): "))


    def calcularBonus(totalVendas):
        salarioBonus = 0.0
        salarioBonus = totalVendas * 0.15
        salarioBonus = valorSalarioFixo + salarioBonus
        return salarioBonus

    salarioVendedor = calcularBonus(totalDeVendaMes)

    salarioVendedor = "{:.2f}".format(salarioVendedor)

    print("\n")
    print(f"TOTAL = {salarioVendedor}")

    print("\n------------------------------------------------")
    continuar = " "
    print("Para continuar tecle enter! ")
    print("Para encerrar digite: (nao) ")
    print("\n")
    continuar = input("Deseja continuar? : ")
    
    if(continuar == "nao"):
        break

