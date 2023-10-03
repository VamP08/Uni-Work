#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void BubbleSort(int arr[],int n){
    for(int i=0;i<n-1;i++){
        for(int j=0;j<n-i-1;j++){
            if (arr[j]>arr[j+1]){
                int temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
        }
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
    BubbleSort(arr,n);
    printf("Sorted Array: \n");
    for(int i=0;i<n;i++){
        printf("%d ",arr[i]);
    }
}