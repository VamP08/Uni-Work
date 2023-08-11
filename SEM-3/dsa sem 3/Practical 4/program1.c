#include <stdio.h>

int top=-1;
int stack[5];

int push(int value){
    if (top==4){
        printf("Stack Overflow");
    }
    else{
        top++;
    stack[top]=value;
    }
}

int pop(){
    if (top==-1){
    printf("Stack Underflow");
    }
    else{
        top--;
    }
}

void display(){
    for(int i=0;i<top;i++){
        printf("%d ",stack[i]);
    }
}

void main(){
    int n;
    int run=0;
    while (run==0){
        printf("1.) Push\n2.) Pop\n3.)Display\n4.) Exit\n");
        printf("Enter choice: ");
        scanf("%d",&n);
        switch(n){
        
        case (1):
            int num;
            printf("Enter Element: ");
            scanf("%d",&num);
            push(num);
            break;
        case (2):
            pop();
            break;
        case (3):
            display();
            break; 
        case (4):
            run=1;
            break;
        }
    }
}
