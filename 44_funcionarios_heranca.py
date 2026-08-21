'''Nível: Intermediário/Avançado

Conceitos:

Herança
Classe base
Classes derivadas
super()
Sobrescrita de métodos

Objetivo: criar uma classe Funcionario e duas especializações: Desenvolvedor e Gerente.'''

# Sistema de funcionários utilizando herança

class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R$ {self.salario:.2f}")


class Desenvolvedor(Funcionario):

    def __init__(self, nome, salario, linguagem):
        super().__init__(nome, salario)
        self.linguagem = linguagem

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Linguagem principal: {self.linguagem}")


class Gerente(Funcionario):

    def __init__(self, nome, salario, equipe):
        super().__init__(nome, salario)
        self.equipe = equipe

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Tamanho da equipe: {self.equipe} pessoas")


desenvolvedor = Desenvolvedor(
    "Carlos",
    5000,
    "Python"
)

gerente = Gerente(
    "Ana",
    8000,
    10
)

print("===== DESENVOLVEDOR =====")
desenvolvedor.exibir_informacoes()

print("\n===== GERENTE =====")
gerente.exibir_informacoes()
