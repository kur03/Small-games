/*#include <stdio.h>
#include <stdlib.h>

#define NBLIN 10
#define NBCOL 10


void initArray(int nbLin, int nbCol, int iArray[nbLin][nbCol], int value)
{
    for(int i=0; i<nbLin; i++)
    {
        for(int j=0; j<nbCol; j++)
        {
            iArray[i][j]=value;
        }
    }
}

int runAstep(int nbLin, int nbCol, int board[nbLin][nbCol], int numPlayer)
{
    int force = getUnitForce();
    printf("\n### Player %d ###\nYour next Unit Force is %d", numPlayer, force);
    if(numPlayer == 2)
    {
        force = force*(-1);
    }
    placeUnitForce(nbLin, nbCol, board, force);
    affectNeighborhood(nbLin, nbCol, board, avoir);
    return 0;
}

int getNextUnitForce()
{
    srand(time(NULL));
    int force = rand() % 19+1;
    return force;
}

void placeUnitForce(int nbLin, int nbCol, int board[nbLin][nbCol], int force)
{
    int x, y;
    printf("Enter the coordinates x and y of the case you want to put your UF on: ");
    scanf("%d %d", &x, &y);
    if((x > (nbLin-1)) || (y > (nbCol-1)) || (board[x][y] != 0))
    {
        while((x > (nbCol-1)) || (y > (nbCol-1)))
        {
            printf("Wrong coordinates (outside of the board), please re-try.\n");
            scanf("%d %d", &x, &y);
        }

        while(board[x][y] != 0)
        {
            printf("\nCell already full, please re-try.\n");
            scanf("%d %d", &x, &y);
        }
    }

    board[x][y] = force;
}

void affectNeighborhood(int nbLin, int nbCol, int board[nbLin][nbCol], int groundLin, int groundCol)
{
    if(board[groundLin][groundCol] > 0)
    {
        for(int i = (groundLin-1); i <= (groundLin+1); i++)
        {
            for(int j = (groundCol-1); j <= (groundCol+1); j++)
            {
                if(board[i][j] > 0)
                {
                    board[i][j]++; 
                }
                else
                {
                    if(board[i][j] < board[groundLin][groundCol])
                    {
                        board[i][j] = board[i][j]*(-1);
                    }
                }

            }
        }
    }

    else if(board[groundLin][groundCol] < 0)
    {
        for(int i = (groundLin-1); i <= (groundLin+1); i++)
        {
            for(int j = (groundCol-1); j <= (groundCol+1); j++)
            {
                if(board[i][j] < 0)
                {
                    board[i][j]--; 
                }
                else
                {
                    if(board[i][j] < board[groundLin][groundCol])
                    {
                        board[i][j] = board[i][j]*(-1);
                    }
                }

            }
        }
    }
}

int getNumberOfTerritoriersForPlayer(int nbLin, int nbCol, int board[nbLin][nbCol], int numPlayer)
{
    for(int i = 0; i < nbLin; i++)
    {
        for(int j = 0; j < nbCol; j++)
        {
            printf("");
        }
    }
}

int runGame(int nbLin, int nbCol, int board[nbLin][nbCol])
{
    int coups = 0;
    int J1 = 1, J2 = 2;
    do
    {
        coups++;
    }
    while(coups <= (nbLin*nbCol));
    
    return 0;
}

int main()
{
    int board[NBLIN][NBCOL];
    initArray(NBLIN, NBCOL, board, 0);
    //showArray(NBLIN, NBCOL, board);
    showBoard(NBLIN, NBCOL, board);
    int winner = runGame(NBLIN, NBCOL, board);
    endOfGame(winner);
    return 0;
}*/