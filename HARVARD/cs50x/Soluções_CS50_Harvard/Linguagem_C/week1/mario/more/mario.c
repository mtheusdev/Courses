/* Matheus Henrique dos Santos, https://github.com/mtheusdev  UDESC CCT CS50X - HARVARD*/
#include <cs50.h>
#include <stdio.h>

/* Contrução de um componente do cenario de um dos jogos mais famosos do mundo
Mario World
Neste algoritmo desenharemos uma piramide com hash's "#" atraves de um calculo de matriz*/

void desenhaPiramide(int n);

int main(void)
{
    int height = 0;

    do
    {
        height = get_int("Height: ");
    }
    while (!(height >= 1 && height <= 8));

    desenhaPiramide(height);
}


void spaceBranco(int l)
{
    for (int k = 0; k < l; k++)
    {
        printf(" ");
    }
}


void desenhaPiramide(int n)
{
    for (int i = 0; i < n; i++)
    {
        spaceBranco(n - i - 1);

        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }

        spaceBranco(2);

        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }


        printf("\n");
    }
}
