/*To calculate the area of the triangle*/
#include<stdio.h>
#include<conio.h>
int area(int,int,int,int);
void main()
{
clrscr();
int a,b,c,d,s;
printf("Enter the 3 sides of the triangle");
scanf("%d%d%d",&a,&b,&c);
s=(a+b+c)/2;
printf("\nthe value of semi perimeter is %d",s);
d=s*(s-a)*(s-b)*(s-c);
printf("\nThe value of d is %d",d);
getch();
}
int area(int x,int y,int z,int r)
{
int w;
w=r*(r-x)*(r-y)*(r-z);
return w;
}