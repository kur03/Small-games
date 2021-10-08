#include <stdio.h>
#include <stdlib.h>

#define NBLIN 6
#define NBCOL 7
int runAstep();
int getColumnForPawn();
int placePawn();
int checkFourLine();
int runGame();
int main();


void clearscreen()
{
    printf("%c[2J", 0x1B);
    printf("%c[%d;%dH", 0x1B, 1, 1);
}

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

void showBoard(int nbLin, int nbCol, int board[nbLin][nbCol])
{
    clearscreen();
    printf("\n### PUISSANCE 4 ###\n\n");
    for(int i=0; i<nbLin; i++)
    {
        for(int j=0; j<nbCol; j++)
        {
            printf("|"); 
            if (board[i][j] == 1)
            {
                printf("\033[31;01m o\033[00m");
            }
            else if (board[i][j] == 2)
            {
                printf("\033[36;01m o\033[00m");
            }

            else
            {
                printf("  ");
            } 
        }
        printf("|\n");
    }
    for(int i = 0; i < nbCol; i++)
    {
        printf(" --");
    }
    printf("\n");
    for(int i = 0; i < nbCol; i++)
    {
        printf(" %d ", i);
    }
}

int runAstep(int nbLin, int nbCol, int board[nbLin][nbCol], int numPlayer)
{
    printf("\n\n### Player %d it's your turn ###\n\n", numPlayer);
    int col = getColumnForPawn(nbLin, nbCol, board);
    int lin = placePawn(nbLin, nbCol, board, col, numPlayer);
    showBoard(nbLin, nbCol, board);
    int fin = checkFourLine(nbLin, nbCol, board, lin, col, numPlayer);
    return fin;
}

int getColumnForPawn(int nbLin, int nbCol, int board[nbLin][nbCol])
{
    int col;
    printf("Enter the number of the column you want to put your pawn on : ");
    scanf("%d", &col);
    if((col > (nbCol-1)) || (col < 0) || (board[0][col] == 1) ||(board[0][col] == 2) )
    {
        while((col > (nbCol-1)) || (col < 0))
        {
            printf("Wrong number of column (outside of the board), please re-try.\n");
            scanf("%d", &col);
        }

        while((board[0][col] == 1) || (board[0][col] == 2))
        {
            printf("\nThis coloumn is full so you can't add any more pawn, please re-try.\n");
            scanf("%d", &col);
        }
    }
    return col;
}

int placePawn(int nbLin, int nbCol, int board[nbLin][nbCol], int pawnCol, int player)
{
    int i = (nbLin-1);
    while(board[i][pawnCol] != 0)
    {
        i--;
    }
    board[i][pawnCol] = player;
    return i; 
}

int checkFourLine(int nbLin, int nbCol, int board[nbLin][nbCol], int pawnLin, int pawnCol, int player)
{
    //column
    int check = 1;
    int i = 1;
    while((board[pawnLin+i][pawnCol] == player) && (i <= 4) && (pawnLin+i <= 5))
    {
        check ++;
        i++;
    }

    i = 1;
    while((board[pawnLin-i][pawnCol] == player) && (i <= 4))
    {
        check ++;
        i++;
    }

    if (check >= 4)
        return 0;
    
    //line
    check = 1;
    i = 1;
    while((board[pawnLin][pawnCol+i] == player) && (i <= 4) && (pawnCol+i <= 6))
    {
        check ++;
        i++;
    }

    i = 1;
    while((board[pawnLin][pawnCol-i] == player) && (i <= 4) && (pawnCol-i >= 0))
    {
        check ++;
        i++;
    }

    if (check >= 4)
        return 0;

    //diagonal
    check = 1;
    i = 1;
    while((board[pawnLin+i][pawnCol+i] == player) && (i <= 4) && (pawnCol+i <= 6) && (pawnLin+i <= 5))
    {
        check ++;
        i++;
    }

    i = 1;
    while((board[pawnLin-i][pawnCol-i] == player) && (i <= 4) && (pawnCol-i >= 0) && (pawnLin-i <= 5))
    {
        check ++;
        i++;
    }

    if (check >= 4)
        return 0;

    check = 1;
    i = 1;
    while((board[pawnLin-i][pawnCol+i] == player) && (i <= 4) && (pawnCol+i <= 6) && (pawnLin-i <= 5))
    {
        check ++;
        i++;
    }

    i = 1;
    while((board[pawnLin+i][pawnCol-i] == player) && (i <= 4) && (pawnCol-i >= 0) && (pawnLin+i <= 5))
    {
        check ++;
        i++;
    }

    if (check >= 4)
        return 0;

    return 1;
}

int runGame(int nbLin, int nbCol, int board[nbLin][nbCol])
{
    int fin = 1;
    int coups = 0;
    int J1 = 1, J2 = 2;
    int winner;
    
    do
    {
        fin = runAstep(nbLin, nbCol, board, J1);
        coups ++;
        if(fin == 1)
        {
            fin = runAstep(nbLin, nbCol, board, J2);
            coups ++;
        }
    }
    while((fin == 1) && (coups <= (nbLin*nbCol)));

    if(coups == (nbLin*nbCol))
    {
        winner = 3;
    }
    else if ((coups%2) == 0)
    {
        winner = 2;
    }
    else
    {
        winner = 1;
    }
    
    return winner;
}

void endOfGame(int winner)
{
    printf("\n\n### THE GAME IS OVER ###\n");
    if((winner == 1) || (winner == 2))
    {
        printf("\nAnd the winner is Player %d !\n", winner);
    }
    else /*if (winner == 3)*/
    {
        printf("\nIt's a draw!\n");
    }  

    char answer[2];
    printf("Do you wanna play again ? (Yes/No) ");
    scanf("%s", answer);
    while((answer[0] != 'y') && (answer[0] != 'Y') && (answer[0] != 'n') && (answer[0] != 'N'))
    {
      scanf("%s", answer);
    }

    if((answer[0] == 'Y') || (answer[0] == 'y'))
        main();
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
}