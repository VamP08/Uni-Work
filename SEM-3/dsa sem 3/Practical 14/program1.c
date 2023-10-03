#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void InsertionSort(int arr[],int n){
    for(int i=1;i<n;i++){
        int current=arr[i];
        int j=i-1;
        while (arr[j]>current && j>=0){
            arr[j+1]=arr[j];
            j--;
        }arr[j+1]=current;
    }
}

int main(){
    int n;
    printf("Enter Length of Array: ");
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++){
        printf("Enter element: ");
        scanf("%d",&arr[i]);
    }
    InsertionSort(arr,n);
    printf("Sorted Array: \n");
    for(int i=0;i<n;i++){
        printf("%d ",arr[i]);
    }
}