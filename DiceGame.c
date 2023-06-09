#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){
  char name[30];
  printf("What your name?\n");
  scanf("%s", name);
  printf("Hello %s!\n", name);
  return 0;
}
