#include<stdio.h>
#include<conio.h>

void main()
{
    int num1, num2, temp;
    printf("Enter the first and the second number: ");
    scanf("%d%d", &num1, &num2);
    temp = num1;
    num1 = num2;
    num2 = temp;
    printf("The first number is %d and the second number is %d", num1, num2);
}