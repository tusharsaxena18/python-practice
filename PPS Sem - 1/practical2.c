#include<stdio.h>
#include<conio.h>
#include<math.h>

void main()
{
    // clrscr();
    float principal, rate, time, si, ci, amount_ci;
    printf("Enter the Principal amount, Rate and Time: ");
    scanf("%f%f%f", &principal, &rate, &time);
    si = (principal*rate*time)/100;
    amount_ci = principal*(pow((1 + (rate/100)),time));
    ci = amount_ci - principal; 
    printf("The simple interest is %f and the compound interest is %f", si, ci);
    getch();
}