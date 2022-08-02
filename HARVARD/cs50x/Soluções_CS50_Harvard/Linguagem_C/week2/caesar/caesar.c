/* Matheus Henrique dos Santos, https://github.com/mtheusdev  UDESC CCT CS50X - HARVARD*/
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>

// Algoritmo classico cifra de cesar

int main(int argc, string argv[])
{
    int chave = 0;
    if (argc == 2)
    {
        chave = atoi(argv[1]);
    }
    if (chave >= 26)
    {
        chave %= 26;
    }
    if (argc != 2 || chave <= 0)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    string entrada = get_string("plaintext: ");
    if (argc == 2)
    {
        for (int i = 0, n = strlen(entrada); i < n; i++)
        {

            if (entrada[i] >= 65 && entrada[i] <= 90)
            {

                if (entrada[i] + chave > 90)
                {
                    entrada[i] -= 26;
                }

                entrada[i] += chave;
            }

            else if (entrada[i] >= 97 && entrada[i] <= 121)
            {

                if (entrada[i] + chave > 121)
                {
                    entrada[i] -= 26;
                }

                entrada[i] += chave;
            }
        }
    }


    printf("ciphertext: %s\n", entrada);
    return 0;
}
