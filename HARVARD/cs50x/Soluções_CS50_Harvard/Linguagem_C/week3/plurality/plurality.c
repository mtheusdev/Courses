/* Matheus Henrique dos Santos, https://github.com/mtheusdev  UDESC CCT CS50X - HARVARD*/
#include <cs50.h>
#include <stdio.h>
#include <string.h>
//Implemente um programa que execute uma eleição de pluralidade


/* Talvez a maneira mais simples de realizar uma eleição, no entanto, seja por meio de um método conhecido como “voto da pluralidade”
(também conhecido como “primeiro após o post” ou “vencedor leva tudo”). Na votação da pluralidade, todo eleitor começa a votar em um candidato.
 No final da eleição, o candidato que tiver o maior número de votos é declarado vencedor.*/
#define MAX 9

typedef struct
{
    string nome;
    int votos;
}
pessoa;


pessoa pessoas[MAX];


int pessoa_count;


bool vote(string nome);
void print_winner(void);

int main(int argc, string argv[])
{

    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    pessoa_count = argc - 1;
    if (pessoa_count > MAX)
    {
        printf("Maximum number of candidate is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < pessoa_count; i++)
    {
        pessoas[i].nome = argv[i + 1];
        pessoas[i].votos = 0;
    }

    int voter_count = get_int("Number of voters: ");

    for (int i = 0; i < voter_count; i++)
    {
        string nome = get_string("Vote: ");


        if (!vote(nome))
        {
            printf("Invalid vote.\n");
        }
    }

    print_winner();
}

bool vote(string nome)
{
    for (int i = 0; i < pessoa_count; i++)
    {
        if (strcmp(nome,  pessoas[i].nome) == 0)
        {
            pessoas[i].votos++;
            return true;
        }
    }
    return false;
}

void print_winner(void)
{
    int votosWinner = 0;


    for (int i = 0; i < pessoa_count; i++)
    {
        if (pessoas[i].votos > votosWinner)
        {
            votosWinner = pessoas[i].votos;
        }
    }


    for (int j = 0; j < pessoa_count; j++)
    {
        if (pessoas[j].votos == votosWinner)
        {
            printf("%s\n", pessoas[j].nome);
        }
    }

    return;
}
