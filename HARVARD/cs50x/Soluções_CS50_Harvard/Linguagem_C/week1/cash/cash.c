
/* Matheus Henrique dos Santos, https://github.com/mtheusdev  UDESC CCT CS50X - HARVARD*/
#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    float dollars;
    do
    {
        dollars = get_float("Change owed in dollars: ");
    }
    while (dollars <= 0); // loop entrada errada
    int coins = 0;
    int cents = round(dollars * 100);  // transformando para centavos
    while (cents > 0)
    {
        if (cents >= 25)
        {
            cents -= 25;
            coins++; // moedas 25
        }
        else if (cents >= 10)
        {
            cents -= 10;
            coins++; //moedas 10
        }
        else if (cents >= 5)
        {
            cents -= 5;
            coins++; // moeda 5
        }
        else
        {
            cents -= 1;
            coins++;
        }
    }
    printf("you are owed %i coins\n", coins); // Quantas moedas totais
}
