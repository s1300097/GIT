#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){
  int num1, num2, total;
  srand(time(NULL));
  num1 = rand() % 6 + 1;
  num2 = rand() % 6 + 1;
  total =  num1 + num2;
  printf("Rolling Dice,,,\nDie 1: %d\nDie 2: %d\nTotal value: %d\nyou ",\
	 num1, num2, total);
  if(total >= 7) printf("Won!\n");
  else printf("lose.\n");
  return 0;
}
