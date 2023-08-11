#include <stdio.h>
struct employee{
    char Name[10];
    int salary;
};

void main(){
    struct employee e1;
    printf("Enter Name of Employee:");
    getchar();
    scanf("%s",e1.Name);
    printf("Enter Salaray of Employee: ");
    scanf("%d",&e1.salary);
    printf("Name of the Employee : %s",e1.Name);
    printf("\nSalary of the Employee : %d",e1.salary);   
}