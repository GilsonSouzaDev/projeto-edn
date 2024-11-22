
cod_item, quant_item = map(int,input("Adicione o codigo e a quantidade de itens: ").split())

def calcularVenda(quant, preco):
    return quant * preco

if cod_item == 1:
    preco = 4.00
    resultado = calcularVenda(quant_item, preco)

if cod_item == 2:
    preco = 4.50
    resultado = calcularVenda(quant_item, preco)

if cod_item == 3:
    preco = 5.00
    resultado = calcularVenda(quant_item, preco)

if cod_item == 4:
    preco = 2.00
    resultado = calcularVenda(quant_item, preco)

if cod_item == 5:
    preco = 1.50
    resultado = calcularVenda(quant_item, preco)

if 0 >= cod_item >= 6:
    print("Codigo invalido")

print(f"Total: R$ {resultado:.2f}")