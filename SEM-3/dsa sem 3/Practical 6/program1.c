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

void insert_at_start(){
    p=malloc(sizeof(struct node));
    int ele;
    printf("Enter value : ");
    scanf("%d",&ele);
    p->val=ele;
    p->next=start;
    start=p;
}

void insert_at_end(){
    p=malloc(sizeof(struct node));
    temp=malloc(sizeof(struct node));
    int ele;
    printf("Enter value : ");
    scanf("%d",&ele);
    temp=start;
    while (temp->next){
        temp=temp->next;    
    }
    temp->next=p;
    p->val=ele;
    p->next=NULL;
}

void display(){
    temp=malloc(sizeof(struct node));
    temp=start; 
    while (temp->next!=NULL){
        printf("%d ",temp->val);
        temp=temp->next;    
    }
    printf("%d",temp->val);
}

void main(){
    create();
    insert_at_start();
    insert_at_start();
    insert_at_start();
    insert_at_start();
    display();
}