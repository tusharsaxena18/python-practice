// WAP TO _______________________________________________________________
#include<stdio.h>
#include<conio.h>

int main()
{
    float subject1, subject2, subject3, subject4, subject5, sum, percentage;
    printf("Enter the marks of all 5 subjects: ");
    scanf("%f%f%f%f%f", &subject1, &subject2, &subject3, &subject4, &subject5); // Asking for user input
    sum = subject1 + subject2 + subject3 + subject4 + subject5; // Calculating the sum of all 5 subjects
    percentage = (sum / 500)*100; // Calculating the percentage
    printf("The sum of the marks for all subjects is %f and the percentage is %f", sum, percentage);
    getch();
    return 0;
}