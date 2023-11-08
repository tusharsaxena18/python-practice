#include<stdio.h>
#include<conio.h>

int add()
{
    int num1, num2, sum;
    printf("Enter two Numbers: ");
    scanf("%d%d",&num1,&num2);
    sum = num1 + num2;
    return sum;

}

void main()
{
    int result;
    result = add();
    printf("The sum of the two numbers is -> %d", result);
    getch();
}