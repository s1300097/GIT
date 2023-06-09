#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){
  int num1, num2;
  srand(time(NULL));
  num1 = rand() % 6 + 1;
  num2 = rand() % 6 + 1;
  printf("Rolling Dice,,,\nDie 1: %d\nDie 2: %d\nTotal value: %d\n",\
	 num1, num2, num1 + num2);
  return 0;
}
