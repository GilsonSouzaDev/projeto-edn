codigoDoFuncionario = 0
quantidaDeHorasTrabalhadas = 0
valorSalarioHora = 0.0

salarioFuncionario = 0.0

while True:

    print("\n------------------------------------------------")
    codigoDoFuncionario = int(input("Digite o codigo do funcionario: "))
    quantidaDeHorasTrabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
    valorSalarioHora = float(input("Digite o valor do salario do funcionario: "))


    def calcularSalario(horas, valor):
        salario = 0.0
        salario = horas * valor
        return salario

    salarioFuncionario = calcularSalario(quantidaDeHorasTrabalhadas, valorSalarioHora)

    salarioFuncionario = "{:.2f}".format(salarioFuncionario)

    print("\n")
    print(f"NUMBER = {codigoDoFuncionario}")
    print(f"SALARY = U$ {salarioFuncionario}")

    print("\n------------------------------------------------")
    continuar = " "
    print("Para continuar tecle enter! ")
    print("Para encerrar digite: (nao) ")
    print("\n")
    continuar = input("Deseja continuar? : ")
    
    if(continuar == "nao"):
        break

