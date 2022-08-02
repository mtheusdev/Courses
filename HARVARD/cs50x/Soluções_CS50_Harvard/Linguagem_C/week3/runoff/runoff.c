/* Matheus Henrique dos Santos, https://github.com/mtheusdev  UDESC CCT CS50X - HARVARD*/
#include <cs50.h>
#include <stdio.h>
#include <string.h>

#define MAX_VOTERS 100
#define MAX_candidatoS 9


int preferences[MAX_VOTERS][MAX_candidatoS];


typedef struct
{
    string nome;
    int votos;
    bool eliminated;
}
candidato;


candidato candidatos[MAX_candidatoS];


int voter_count;
int candidato_count;


bool vote(int voter, int rank, string nome);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{

    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }


    candidato_count = argc - 1;
    if (candidato_count > MAX_candidatoS)
    {
        printf("Maximum number of candidates is %i\n", MAX_candidatoS);
        return 2;
    }
    for (int i = 0; i < candidato_count; i++)
    {
        candidatos[i].nome = argv[i + 1];
        candidatos[i].votos = 0;
        candidatos[i].eliminated = false;
    }

    voter_count = get_int("Number of voters: ");
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }


    for (int i = 0; i < voter_count; i++)
    {


        for (int j = 0; j < candidato_count; j++)
        {
            string nome = get_string("Rank %i: ", j + 1);


            if (!vote(i, j, nome))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }

        printf("\n");
    }


    while (true)
    {

        tabulate();


        bool won = print_winner();
        if (won)
        {
            break;
        }


        int min = find_min();
        bool tie = is_tie(min);


        if (tie)
        {
            for (int i = 0; i < candidato_count; i++)
            {
                if (!candidatos[i].eliminated)
                {
                    printf("%s\n", candidatos[i].nome);
                }
            }
            break;
        }


        eliminate(min);


        for (int i = 0; i < candidato_count; i++)
        {
            candidatos[i].votos = 0;
        }
    }
    return 0;
}


bool vote(int voter, int rank, string nome)
{
    for (int i = 0; i < candidato_count; i++)
    {
        if (strcmp(nome,  candidatos[i].nome) == 0)
        {
            preferences[voter][rank] = i;
            return true;
        }
    }
    return false;
}


void tabulate(void)
{
    for (int j = 0; j < voter_count; j++)
    {
        int i = 0;

        while (candidatos[preferences[j][i]].eliminated)
        {
            i++;
        }

        candidatos[preferences[j][i]].votos++;
    }
    return;
}


bool print_winner(void)
{
    for (int j = 0; j < candidato_count; j++)
    {
        if (candidatos[j].votos > voter_count / 2)
        {
            printf("%s\n", candidatos[j].nome);
            return true;
        }
    }
    return false;
}


int find_min(void)
{
    int minimumvotos = 101;
    for (int i = 0; i < candidato_count; i++)
    {
        if (!candidatos[i].eliminated)
        {
            if (candidatos[i].votos < minimumvotos)
            {
                minimumvotos = candidatos[i].votos;
            }
        }
    }
    return minimumvotos;
}


bool is_tie(int min)
{
    int votosWinner = 0;

    for (int j = 0; j < candidato_count; j++)
    {
        if (candidatos[j].votos > votosWinner)
        {
            votosWinner = candidatos[j].votos;
        }
    }

    for (int i = 0; i < candidato_count; i++)
    {
        if (!candidatos[i].eliminated)
        {
            if (candidatos[i].votos < votosWinner)
            {
                return false;
            }
        }
    }
    return true;
}


void eliminate(int min)
{
    for (int i = 0; i < candidato_count; i++)
    {
        if (candidatos[i].votos == min)
        {
            candidatos[i].eliminated = true;
        }
    }

    return;
}
