#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    char input[40];
    char flag[17] = "}gn1rts_t4mr0f{";

    srand(time(NULL));
   
    printf("What is your name: ");
    scanf("%s", &input);

   while (true) {
    system("cls");
    printf("+---------------------------+\n"); 
    printf("|         Welcome!          |\n");
    printf("| Here you can roll a dice  |\n");
    printf("+---------------------------+\n");

    printf("Hello, ");
    printf(input);

    printf("\n\n1 - roll the dice");
    printf("\n2 - exit\n");

    int choice = 2;
    scanf("%d", &choice);

    if (choice == 1) {
        printf("The result of the throw: %d\n", (1 + rand()%6));

        printf("\nEnter something to continue ");
        scanf("%d", &choice);
    }
    else
        exit(0);
   }
   
   return 0;
}