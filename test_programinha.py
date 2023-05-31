from programinha import Pessoa, Aluno, Professor

def test_pessoa():
    pessoa = Pessoa("João", 30)
    assert pessoa.nome == "João"
    assert pessoa.idade == 30

def test_aluno():
    aluno = Aluno("Maria", 20, "1234")
    assert aluno.nome == "Maria"
    assert aluno.idade == 20
    assert aluno.matricula == "1234"

def test_professor():
    professor = Professor("Pedro", 40, "Matemática")
    assert professor.nome == "Pedro"
    assert professor.idade == 40
    assert professor.disciplina == "Matemática"

def test_apresentar_pessoa(capsys):
    pessoa = Pessoa("João", 30)
    pessoa.apresentar()
    out, err = capsys.readouterr()
    assert out == "Olá, meu nome é João e tenho 30 anos.\n"

def test_apresentar_aluno(capsys):
    aluno = Aluno("Maria", 20, "1234")
    aluno.apresentar()
    out, err = capsys.readouterr()
    assert out == '''Olá, meu nome é Maria e tenho 20 anos.\n
                    Eu sou um aluno e minha matrícula é 1234.\n'''

def test_apresentar_professor(capsys):
    professor = Professor("Pedro", 40, "Matemática")
    professor.apresentar()
    out, err = capsys.readouterr()
    assert out == "Olá, meu nome é Pedro e tenho 40 anos.\nEu sou um professor e minha disciplina é Matemática.\n"
