#include <stdio.h>

int main(void) {
	// your code goes here
	long int n,f;
	scanf("%ld",&n);
	if(n==1 || n==2) printf("NO");
	else{
	for(int i=2;i<n;i++){
	    f=0;
	    for(int j=2;j<i;j++){
	        if(i%j==0){
	            f+=1;
	            break;
	        }
	    }
	    if(f==0) printf("%ld ",i);
	}
	}
	return 0;
}

