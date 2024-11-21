class Venda:
    def __init__(self, codigoDaPeca, numeroDePecas, valorDaPeca ):
        self.codigoDaPeca = codigoDaPeca
        self.numeroDePecas = numeroDePecas
        self.valorDaPeca = valorDaPeca

    def calcularVenda(self):
        resultado = 0.0
        resultado = self.numeroDePecas * self.valorDaPeca
        return resultado

ListaDeVendas = []

while True:    
    entrada = input("Digite dois números inteiros e um float, separados por espaço: ")
    codigo, numeroPecas, valorPeca = map(float, entrada.split())
    codigo = int(codigo)
    numeroPecas = int(numeroPecas)

    venda = Venda(codigo, numeroPecas, valorPeca)

    resultado = venda.calcularVenda()

    ListaDeVendas.append(resultado)
    
    

    print("------------------------------------------------")
    continuar = " "
    print("Para adicionar uma venda tecle enter! ")
    print("Para encerrar digite: (nao) ")
    print("\n")
    continuar = input("Deseja continuar? : ")
    
    if(continuar == "nao"):
        break
    

resultadoDaVenda = sum(ListaDeVendas)
resultadoDaVenda = "{:.2f}".format(resultadoDaVenda)

print("\n----------------------------------")
print(f"VALOR A PAGAR: R$ {resultadoDaVenda}")