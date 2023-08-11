#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Queue using a Struct Type
struct Queue {
    int capacity;  
    int rear,front;       
    int* array;   
}*queue;

void create(int n){
    queue=malloc(sizeof(struct Queue));
    queue->front=-1;
    queue->rear=-1;
    queue->capacity=n;
    queue->array=malloc(n * sizeof(int));
}

bool isFull() {
    if (queue->rear == queue->capacity - 1){
        return true;
    }
    return false;
}

bool isEmpty() {
    if (queue->front == -1){
        return true;
    }
    return false;
}

void insert(int item) {
    if (isFull(queue)) {
        printf("Queue Overflow\n");
        return;
    }
    if (queue->front==-1){
        queue->front++;
    }
    queue->array[++queue->rear] = item;
    printf("%d pushed to queue\n", item);
}

int delete() {
    if (isEmpty()) {
        printf("Queue Underflow\n");
        return 0;
    }
    queue->front++;
}

void display() {
    if (isEmpty()) {
        printf("Queue is empty\n");
        return;
    }
    printf("Queue contents: ");
    for (int i = queue->front; i <= queue->capacity; i++) {
        printf("%d ", queue->array[i]);
    }
    printf("\n");
}

int main() {
    create(5);
    insert(10);
    insert(20);
    insert(30);

    display();

    delete();

    display();

    return 0;
}
