/*Balanced String*/
#include<stdio.h>
#include<conio.h>
void main()
{
clrscr();
char a[]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
int i=0,j=0,n,d;
printf("Enter the value of n");
scanf("%d",&n);
d=(n/2);
for(i=0;i<d;i++)
{
for(j=26;j<(26-d);j--)
{
printf("\n%c",a[i]);
}
printf("\n%c",a[j]);
}
getch();
}
