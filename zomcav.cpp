#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        int flag=0;
        cin>>n;
        long long int c[n];
        long long int m[n]={0};
        long long int h[n],j=0,k=0;
        for(int i=0;i<n;i++)
            cin>>c[i];
        for(int i=0;i<n;i++)
            cin>>h[i];
         sort(h,h+n);
         if(h[n-1]>n)
         {
             cout<<"NO"<<endl;
             break;
         }
        for(int i=0;i<n;i++)
        {
            j=i-c[i];
            k=i+c[i];
            if(j<0)
            {
                j=0;
            }
            if(n<k)
                k=n;
            for(int p=j;p<k;p++)
            {
                m[p]++;
            }
        }

        sort(m,m+n);
        for(int i=0;i<n;i++)
        {
            if(m[i]!=h[i])
            {
                flag=1;
                break;
            }
        }
        if(flag==0)
            cout<<"YES"<<endl;
        else
            cout<<"NO"<<endl;
    }

}
