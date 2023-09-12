#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int binarySearch(int arr[], int size, int key) {
    int start = 0;
    int end = size;

    while (start <= end) {
        int mid = (start + end) / 2;

        if (arr[mid] == key) {
            return mid; 
        }

        if (arr[mid] < key) {
            start = mid + 1;
        }
        else {
            end = mid - 1;
        }
    }return -1;
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
    int key;
    printf("Enter element you need to find: ");
    scanf("%d",&key);
    int result = binarySearch(arr, n, key);

    if (result != -1) {
        printf("Element %d found at index %d\n", key, result);
    } else {
        printf("Element %d not found in the array\n", key);
    }

}