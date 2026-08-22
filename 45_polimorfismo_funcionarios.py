'''Nível: Avançado inicial

Conceitos:

Polimorfismo
Herança
Classes
Sobrescrita de métodos
Listas de objetos
for

Objetivo: criar diferentes tipos de funcionários e permitir que o mesmo método seja executado de maneira diferente dependendo do objeto.'''

# Polimorfismo utilizando funcionários


class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * 0.10

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R$ {self.salario:.2f}")
        print(f"Bônus: R$ {self.calcular_bonus():.2f}")


class Desenvolvedor(Funcionario):

    def __init__(self, nome, salario, linguagem):
        super().__init__(nome, salario)
        self.linguagem = linguagem

    def calcular_bonus(self):
        return self.salario * 0.15


class Gerente(Funcionario):

    def __init__(self, nome, salario, equipe):
        super().__init__(nome, salario)
        self.equipe = equipe

    def calcular_bonus(self):
        return self.salario * 0.20


funcionarios = [
    Desenvolvedor("Carlos", 5000, "Python"),
    Gerente("Ana", 8000, 10),
    Desenvolvedor("João", 6000, "Java")
]


for funcionario in funcionarios:
    funcionario.exibir_informacoes()
    print()
    