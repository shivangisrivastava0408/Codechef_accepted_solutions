#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int min=-1;
        int n,m,k,l,r;
        cin>>n>>m>>k>>l>>r;
        int c[n],p[n];
        for(int i=0;i<n;i++)
        {
            cin>>c[i]>>p[i];
        }
        for(int i=0;i<n;i++)
        {
            if(c[i]>k+1)
            {
                if((c[i]-m)>=k)
                    c[i]=c[i]-m;
                else
                    c[i]=k;
            }
            else
            {
                if((c[i]-m)<=k)
                    c[i]=c[i]+m;
                else
                    c[i]=k;

            }
        }

        for(int i=0;i<n;i++)
        {
            if(l<=c[i] && c[i]<=r)
            {
                if(min>p[i] || min== -1)
                    min=p[i];

            }
        }
        cout<<min<<endl;

    }
}
