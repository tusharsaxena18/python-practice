#include<stdio.h>
#include<conio.h>
#include<math.h>

void main()
{
    float radius, area, circumference;
    printf("Enter the radius of the circle: ");
    scanf("%f", &radius);
    area = 3.14*pow(radius, 2);
    circumference = 2 * 3.14 * radius;
    printf("The area of the circle is %f and the circumference is %f", area, circumference);
}  