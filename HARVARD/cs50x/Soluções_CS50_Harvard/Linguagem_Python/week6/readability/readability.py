# Matheus Henrique dos Santos, https://github.com/mtheusdev  UDESC CCT CS50X - HARVARD
from cs50 import get_string


entrada = get_string("entrada: \n")

letras = 0
palavras = 0
sentences = 0
contador = 0

for i in entrada:
    contador += 1

for i in range(contador):
    if (ord(entrada[i]) >= 65 and ord(entrada[i]) <= 122):
        letras += 1

    elif (ord(entrada[i]) == 32 and (ord(entrada[i - 1]) != 33 and ord(entrada[i - 1]) != 46 and ord(entrada[i - 1]) != 63)):
        palavras += 1
    elif (ord(entrada[i]) == 33 or ord(entrada[i]) == 46 or ord(entrada[i]) == 63):
        sentences += 1
        palavras += 1

L = letras * 100 / palavras
S = sentences * 100 / palavras

index = round(0.0588 * L - 0.296 * S - 15.8)

if (index < 1):
    print("Before Grade 1")

elif (index >= 16):
    print("Grade 16+")

else:
    print(f"Grade {index}")
