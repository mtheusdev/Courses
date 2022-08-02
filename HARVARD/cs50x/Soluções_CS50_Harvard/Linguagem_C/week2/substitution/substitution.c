/* Matheus Henrique dos Santos, https://github.com/mtheusdev  UDESC CCT CS50X - HARVARD*/
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>

// Implemente um programa que implemente uma cifra de substituição

/*Uma chave, por exemplo, pode ser a sequência NQXPOMAFTRHLZGECYJIUWSKDVB. Essa chave de 26 caracteres significa que A(a primeira letra do alfabeto)
deve ser convertida em N(o primeiro caractere da chave), B(a segunda letra do alfabeto) deve ser convertida em Q(o segundo caractere da chave) e assim por diante.*/
int main(int argc, string argv[])
{

    if (argc != 2 || strlen(argv[1]) != 26)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    char alfabeto[26];
    char chave[26];

    for (int i = 0; i < 26; i++)
    {
        chave[i] = toupper(argv[1][i]);
        if (chave[i] >= 65 && chave[i] <= 90)
        {
            alfabeto[i] = 65 + i - chave[i];
        }

        else
        {
            printf("Usage: ./substitution key\n");
            return 1;
        }


        for (int j = 0; j < i; j++)
        {
            if (chave[i] == chave[j])
            {
                printf("Usage: ./substitution key\n");
                return 1;
            }
        }
    }

    string entrada = get_string("plaintext: ");


    for (int i = 0, n = strlen(entrada); i < n; i++)
    {
        if (entrada[i] >= 65 && entrada[i] <= 90)
        {
            entrada[i] = entrada[i] - alfabeto[entrada[i] - 65];
        }
        else if (entrada[i] >= 97 && entrada[i] <= 122)
        {
            entrada[i] = entrada[i] - alfabeto[entrada[i] - 97];
        }
    }


    printf("ciphertext: %s\n", entrada);
    return 0;
}
