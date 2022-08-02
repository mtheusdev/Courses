# Matheus Henrique dos Santos, https://github.com/mtheusdev  UDESC CCT CS50X - HARVARD

from cs50 import SQL
from csv import reader
from sys import argv

banco = SQL("sqlite:///students.db")


if len(argv) < 2:
    print("usage error, import.py characters.csv")
    exit()


with open(argv[1], newline='') as charactersFile:
    characters = reader(charactersFile)
    for character in characters:
        if character[0] == 'name':
            continue


        nomeInteiro = character[0].split()
        if len(nomeInteiro) < 3:
            banco.execute("INSERT INTO students(first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                       nomeInteiro[0], None, nomeInteiro[1], character[1], character[2])

        else:
            banco.execute("INSERT INTO students(first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                       nomeInteiro[0], nomeInteiro[1], nomeInteiro[2], character[1], character[2])
