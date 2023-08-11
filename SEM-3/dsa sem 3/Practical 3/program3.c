#include <stdio.h>

struct student {
  char name[50];
  int age;
  float marks;
};

int main() {
  struct student s[5];
  int i;

  printf("Enter information of students:\n");

  for (i = 0; i < 5; ++i) {
    printf("\nFor student %d,\n", i+1);
    printf("Enter name: ");
    scanf("%s", s[i].name);
    printf("Enter age: ");
    scanf("%d", &s[i].age);
    printf("Enter marks: ");
    scanf("%f", &s[i].marks);
  }
  printf("\nDisplaying Information:\n");

  for (i = 0; i < 5; ++i) {
    printf("\nStudent %d\n", i+1);
    printf("Name: %s\n", s[i].name);
    printf("Age: %d\n", s[i].age);
    printf("Marks: %.2f\n", s[i].marks);
  }

  return 0;
}