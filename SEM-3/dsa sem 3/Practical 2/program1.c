//1)
#include <stdio.h>

void main(){
    int n1,n2;
    int i;
    printf("Enter 1st number: ");
    scanf("%d",&n1);
    printf("Enter 2nd number: ");
    scanf("%d",&n2);
    printf("Operation you want to perform:\n1) Addition\n2) Subtraction\n3) Multiplication\n4) Division\n5) Modulus\n Enter the option(1,2,3,4,5): ");
    scanf("%d",&i);

    switch (i){
        case 1:
            printf("Addition = %d",n1+n2);
            break;
        case 2:
            printf("Subtraction = %d",n1-n2);
            break;
        case 3:
            printf("Multiplication = %d",n1*n2);
            break;
        case 4:
            printf("Division = %d",n1/n2);
            break;
        case 5:
            printf("Modulus = %d",n1%n2);
            break;
    }   
}