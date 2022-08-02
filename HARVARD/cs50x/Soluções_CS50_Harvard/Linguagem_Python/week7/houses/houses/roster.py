# Matheus Henrique dos Santos, https://github.com/mtheusdev  UDESC CCT CS50X - HARVARD
from cs50 import SQL
from sys import argv

if len(argv) < 2:
    print("usage error, roster.py houseName")
    exit()


banco = SQL("sqlite:///students.db")
alunos = banco.execute("SELECT * FROM alunos WHERE house = (?) ORDER BY last", argv[1])

for aluno in alunos:
    if aluno['middle'] != None:
        print(f"{aluno['first']} {aluno['middle']} {aluno['last']}, born {aluno['birth']}")
    else:
        print(f"{aluno['first']} {aluno['last']}, born {aluno['birth']}")
