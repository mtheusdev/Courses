/* Matheus Henrique dos Santos, https://github.com/mtheusdev  UDESC CCT CS50X - HARVARD*/
#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Implemente um programa que execute uma eleição Tideman


/*O método de votação Tideman (também conhecido como "pares classificados") é um método de votação de escolha classificada que garante o vencedor da eleição Condorcet, se houver.

De um modo geral, o método Tideman funciona construindo um “gráfico” de candidatos, onde uma seta (ou seja, borda) do candidato A para o candidato B indica que o candidato A vence o candidato B em um confronto direto.*/


#define MAX 9// numero maximo de participantes


int mat[MAX][MAX];


bool locked[MAX][MAX];
bool lock = true;


typedef struct
{
    int vencedor;
    int perdedor;
}
pares;


string candidatos[MAX];
pares paress[MAX * (MAX - 1) / 2];

int pares_count;
int candidato_count;


void validateLock(int j);
int comparator(const void *a, const void *b);
bool vote(int rank, string name, int ranks[]);
void record_mat(int ranks[]);
void add_paress(void);
void sort_paress(void);
void lock_paress(void);
void print_vencedor(void);

int main(int argc, string argv[])
{

    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    candidato_count = argc - 1;
    if (candidato_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidato_count; i++)
    {
        candidatos[i] = argv[i + 1];
    }

    for (int i = 0; i < candidato_count; i++)
    {
        for (int j = 0; j < candidato_count; j++)
        {
            locked[i][j] = false;
            mat[i][j] = 0;
        }
    }

    pares_count = 0;
    int voter_count = get_int("Number of voters: ");

    for (int i = 0; i < voter_count; i++)
    {
        int ranks[candidato_count];

        for (int j = 0; j < candidato_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_mat(ranks);

        printf("\n");
    }

    add_paress();
    sort_paress();
    lock_paress();
    print_vencedor();
    return 0;
}

bool vote(int rank, string name, int ranks[])
{
    for (int i = 0; i < candidato_count; i++)
    {
        if (strcmp(name,  candidatos[i]) == 0)
        {
            ranks[rank] = i;
            return true;
        }
    }
    return false;
}
void record_mat(int ranks[])
{
    for (int i = 0; i < candidato_count; i++)
    {
        for (int j = i + 1; j < candidato_count; j++)
        {
            mat[ranks[i]][ranks[j]]++;
        }
    }
}

void add_paress(void)
{
    for (int i = 0; i < candidato_count; i++)
    {
        for (int j = i + 1; j < candidato_count; j++)
        {
            if (mat[i][j] > mat[j][i])
            {
                paress[pares_count].vencedor = i;
                paress[pares_count].perdedor = j;
                pares_count++;
            }
            else if (mat[i][j] < mat[j][i])
            {
                paress[pares_count].vencedor = j;
                paress[pares_count].perdedor = i;
                pares_count++;
            }
        }
    }
}

int comparator(const void *a, const void *b)
{
    pares *orderA = (pares *)a;
    pares *orderB = (pares *)b;

    return (mat[orderB->vencedor][orderB->perdedor] - mat[orderA->vencedor][orderA->perdedor]);
}

void sort_paress(void)
{
    qsort(paress, pares_count, sizeof(pares), comparator);
}


void validateLock(int j)
{
    if (j == 0)
    {
        return;
    }

    int r = 0;
    bool rank[j];
    for (int i = 0; i < j; i++)
    {
        rank[i] = false;
    }

    validateLock(j - 1);

    for (int i = 0; i < j; i++)
    {
        for (int k = 0; k < j; k++)
        {
            if (locked[i][k] == true)
            {
                rank[i] = true;
            }
        }
    }

    for (int i = 0; i < j; i++)
    {
        if (rank[i] == true)
        {
            r++;
        }
    }
    if (r == j)
    {
        lock = false;
    }
}

void lock_paress(void)
{
    for (int i = 0; i < pares_count; i++)
    {
        locked[paress[i].vencedor][paress[i].perdedor] = true;

        validateLock(candidato_count);

        if (!lock)
        {
            locked[paress[i].vencedor][paress[i].perdedor] = false;
        }
        lock = true;
    }
}

void print_vencedor(void)
{
    int vencedor;
    int rank;

    for (int i = 0; i < candidato_count; i++)
    {
        rank = 0;
        for (int k = 0; k < candidato_count; k++)
        {
            if (locked[k][i] == false)
            {
                rank++;
            }
        }
        if (rank == candidato_count)
        {
            printf("%s\n", candidatos[i]);
        }
    }
}
