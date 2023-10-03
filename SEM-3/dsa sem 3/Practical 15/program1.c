#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void SelectionSort(int arr[],int n){
    for (int i=0;i<n;i++){
        int min_index=i;
        for(int j=i+1;j<n;j++){
            if (arr[min_index]>arr[j]){
                int temp=arr[min_index];
                arr[min_index]=arr[j];
                arr[j]=temp;
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
    SelectionSort(arr,n);
    printf("Sorted Array: \n");
    for(int i=0;i<n;i++){
        printf("%d ",arr[i]);
    }
}