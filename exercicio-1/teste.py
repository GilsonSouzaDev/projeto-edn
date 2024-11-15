class Aluno:
    def __init__(self, nome, idade, area, profissao):
        self.nome = nome
        self.idade = idade
        self.area = area
        self.profissao = profissao


Gilson = Aluno("Gilson", 25, "backend","programador")
Joao = Aluno("Joao", 55, "AWS-cloud", "Analista")
Maria = Aluno("Maria", 35, "AWS-cloud", "Analista")

lista_de_livros = [Gilson, Joao, Maria]


print("\n")
for aluno in lista_de_livros:

    print(f"Nome: {aluno.nome} \t Idade: {aluno.idade} \t Area: {aluno.area}  \tProfissÃ£o: {aluno.profissao}")   
           
