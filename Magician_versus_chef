#include<stdio.h>
int main()
{
    int t;
    long int n,x,s,a,b;
    scanf("%d",&t);
    while(t--){
        scanf("\n%ld%ld%ld",&n,&x,&s);
        for(long int j=0;j<s;j++){
            scanf("\n%ld%ld",&a,&b);
            if(a==x) x=b;
            else if(b==x) x=a;
        }
        printf("\n%ld",x);
    }
    return 0;
}
