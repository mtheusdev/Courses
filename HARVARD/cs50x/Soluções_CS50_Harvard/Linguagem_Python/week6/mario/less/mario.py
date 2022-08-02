# Matheus Henrique dos Santos, https://github.com/mtheusdev  UDESC CCT CS50X - HARVARD
from cs50 import get_int


altura = 0
while (altura> 8 or altura< 1):
    altura= get_int("Height:\n")

for i in range(1, altura + 1):
    print(" " * (altura - i), end="")
    print("#" * (i))
