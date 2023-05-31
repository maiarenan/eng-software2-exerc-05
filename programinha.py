class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
    
    def apresentar(self):
        super().apresentar()
        print(f"Eu sou um aluno e minha matrícula é {self.matricula}.")

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina
    
    def apresentar(self):
        super().apresentar()
        print(f"Eu sou um professor e minha disciplina é {self.disciplina}.")

# Criando instâncias das classes
pessoa = Pessoa("João", 30)
aluno = Aluno("Maria", 20, "1234")
professor = Professor("Pedro", 40, "Matemática")

# Chamando o método apresentar() para cada instância
pessoa.apresentar()
aluno.apresentar()
professor.apresentar()
