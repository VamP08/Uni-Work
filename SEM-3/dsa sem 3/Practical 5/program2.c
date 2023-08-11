#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Stack using a Struct Type
struct Stack {
    int capacity;  
    int top;       
    int* array;   
}*stack;

void create(int n){
    stack=malloc(sizeof(struct Stack));
    stack->top=-1;
    stack->capacity=n;
    stack->array=malloc(n * sizeof(int));
}

bool isFull() {
    if (stack->top == stack->capacity - 1){
        return true;
    }
    return false;
}

bool isEmpty() {
    if (stack->top == -1){
        return true;
    }
    return false;
}

void push(int item) {
    if (isFull()) {
        printf("Stack Overflow\n");
        return;
    }
    stack->array[++stack->top] = item;
    printf("%d pushed to stack\n", item);
}

void pop() {
    if (isEmpty()) {
        printf("Stack Underflow\n");
    }
    stack->top--;
}

void display() {
    if (isEmpty()) {
        printf("Stack is empty\n");
        return;
    }
    printf("Stack contents: ");
    for (int i = stack->top; i >= 0; --i) {
        printf("%d ", stack->array[i]);
    }
    printf("\n");
}

int main() {
    create(5);
    push(10);
    push(20);
    push(30);

    display();

    pop();

    display();

    return 0;
}
