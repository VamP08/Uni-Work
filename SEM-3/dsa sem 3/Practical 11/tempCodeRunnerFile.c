#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main(){
    int n;
    printf("Enter size of the array: ");
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++){
        printf("Enter element: ");
        scanf("%d",&arr[i]);
    }

    int key;
    printf("Enter element to be searched: ");
    scanf("%d",&key);

    bool res=false;
    for(int i=0;i<n;i++){
        if (arr[i]==key){
            res=true;
        }
    }
    if (res==true) printf("Element Found.");
    else printf("Element not found.");
}