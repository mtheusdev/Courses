/* Matheus Henrique dos Santos, https://github.com/mtheusdev  UDESC CCT CS50X - HARVARD*/
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

//Implemente um programa que calcule o nível aproximado necessário para compreender algum entradao
//a formula padrao utilizada é index = 0.0588 * L - 0.296 * S - 15.8
int main(void)
{

    string entrada = get_string("entrada: \n");

    float letras = 0;
    float palavras = 0;
    float sentence = 0;


    for (int i = 0, n = strlen(entrada); i < n; i++)
    {

        if (entrada[i] >= 65 && entrada[i] <= 122)
        {
            letras++;
        }

        else if (entrada[i] == 32 && (entrada[i - 1] != 33 && entrada[i - 1] != 46 && entrada[i - 1] != 63))
        {
            palavras++;
        }

        else if (entrada[i] == 33 || entrada[i] == 46 || entrada[i] == 63)
        {
            sentence++;
            palavras++;
        }
    }

    float L = letras * 100 / palavras;
    float S = sentence * 100 / palavras;
    float index = round(0.0588 * L - 0.296 * S - 15.8);

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", (int) index);
    }
}
