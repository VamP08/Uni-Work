#include <stdio.h>
#include <stdlib.h>

struct node{
    int val;
    struct node*prev;
    struct node*next;
}*start,*p,*temp;

void create(){
    p=malloc(sizeof(struct node));
    int ele;
    printf("Enter value : ");
    scanf("%d",&ele);
    p->val=ele;
    p->next=NULL;
    p->prev=NULL;
    start=p;
}

void insert_at_start(){
    p=malloc(sizeof(struct node));
    int ele;
    printf("Enter value : ");
    scanf("%d",&ele);
    p->val=ele;
    p->next=start;
    p->prev=NULL;
    start=p;
}

void insert_at_end(){
    p=malloc(sizeof(struct node));
    int ele;
    printf("Enter value : ");
    scanf("%d",&ele);
    temp=start;
    while (temp->next){
        temp=temp->next;
    }
    temp->next=p;
    p->val=ele;
    p->prev=temp;
    p->next=NULL;
}

void insert_at_middle(){
    p=malloc(sizeof(struct node));
    int ele;
    printf("Enter value : ");
    scanf("%d",&ele);
    temp=start;
    int n=1;
    while (temp->next){
        n+=1;
        temp=temp->next;
    }
    temp=start;
    for (int i=0;i<(n/2);i++){
        temp=temp->next;    
    }
    p->val=ele;
    p->next=temp->next;
    temp->next=p;
}

void display(){
    temp=malloc(sizeof(struct node));
    temp=start;
    while (temp->next){
        printf("%d ",temp->val);
        temp=temp->next;
    }printf("%d ",temp->val);
}

void main(){
    create();
    insert_at_start();
    insert_at_start();
    insert_at_middle();
    insert_at_middle();
    insert_at_end();
    insert_at_end();
    display();
}