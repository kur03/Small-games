#include "variables.h"
//#include <stdio.h>

void size(int nbr_mine) {
    //9x9 & 10 ; 16x16 & 40 ; 16x30 &99
    if (nbr_mine == 10) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                board[i][j] = 0;
            }
        }
        put_mine(nbr_mine, 9, 9);
    }
    else if (nbr_mine == 40){
        for (int i = 0; i < 16; i++) {
            for (int j = 0; j < 16; j++) {
                board[i][j] = 0;
            }
        }
        put_mine(nbr_mine, 16, 16);
    }
    else {
        for (int i = 0; i < 16; i++) {
            for (int j = 0; j < 30; j++) {
                board[i][j] = 0;
            }
        }
        put_mine(nbr_mine, 16, 30);
    }
}

void put_mine(int nbr_mine, int size_x, int size_y) {
    int temp_mine = nbr_mine;
    while (temp_mine > 0)
    {
        int x = rand() % size_x;
        int y = rand() % size_y;
        if (board[x][y] != 9) {
            board[x][y] = 9;
            printf("mine = %d\n", temp_mine);
            temp_mine --;
        }
    }
    printf("\n");
    for (int i = 0; i < size_x; i ++) {
        for (int j = 0; j < size_y; j++) {
            printf("%d ", board[i][j]);
        }
        printf("\n");
    }

    put_nbr(size_x, size_y);
}


void put_nbr(int size_x, int size_y) {
    int nbr = 0;
    for (int i = 0; i < size_x; i ++) {
        for (int j = 0; j < size_y; j++) {
            if(board[i][j] != 9) {
                // we check the line above
                if (i != 0) { // first line -1 IMPOSSIBLE
                    // top left
                    if ((board[i-1][j-1] == 9) && (j !=0 ))   // first colum j-1 IMPOSSIBLE
                        nbr ++;
                    // top middle
                    if (board[i-1][j] == 9)
                        nbr ++;
                    // top right
                    if ((board[i-1][j+1] == 9) && (j != size_y-1))   // last colum j+1 IMPOSSIBLE
                        nbr ++;
                }

                // we check the line under
                if (i < size_x-1) { // last line +1 IMPISSOBLE
                    // below left
                    if ((board[i+1][j-1] == 9) && (j !=0 ))   // first colum j-1 IMPOSSIBLE
                        nbr ++;
                    // below middle
                    if (board[i+1][j] == 9)
                        nbr ++;
                    // bellow right
                    if ((board[i+1][j+1] == 9) && (j != size_y-1))   // last colum j+1 IMPOSSIBLE
                        nbr ++;
                }
                
                // we check the current line right case
                if ((board[i][j-1] == 9) && (j != 0))   // first colum j-1 IMPOSSIBLE
                    nbr ++;
                // we check the current line left case
                if ((board[i][j+1] == 9) && (j != size_y-1))   // last colum j+1 IMPOSSIBLE
                    nbr ++;
                
                board[i][j] = nbr;
                nbr = 0;
            }
        }

    }
printf("\n\n");
    for (int i = 0; i < size_x; i ++) {
    for (int j = 0; j < size_y; j++) {
        printf("%d ", board[i][j]);
    }
    printf("\n");
    }
}

int main() {
    size(10);
    return 0;
}