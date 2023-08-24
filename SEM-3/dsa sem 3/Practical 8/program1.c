#include <stdio.h>
#include <stdlib.h>

struct node{

    int val;
    struct node*next;

}*start,*p,*temp;

void create(){
    p=malloc(sizeof(struct node));
    int ele;
    printf("Enter value : ");
    scanf("%d",&ele);
    p->val=ele;
    p->next=NULL;
    start=p;
}

void insert(){
    p=malloc(sizeof(struct node));
    int ele;
    printf("Enter value : ");
    scanf("%d",&ele);
    p->val=ele;
    if (start->next==NULL){
        start->next=p;
        p->next=start;
    }
    temp=start->next;
    while (temp->next != start) {
            temp = temp->next;
    }
    temp->next=p;
    p->next=start;
}

void display(){
    struct node *temp;
    temp=start;
    do{
        printf("\n%d",temp->val);
        temp=temp->next;
    }
    while(temp!=start);
}

void main(){
    create();
    insert();
    insert();
    insert();
    insert();
    display();
}