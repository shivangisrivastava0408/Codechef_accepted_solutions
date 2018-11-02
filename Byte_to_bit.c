#include <stdio.h>

int main(void) {
	long int t, n, i, w, a, b, c;
	scanf("%ld",&t);
	while (t--){
	    scanf("%ld",&n);
	    if (n==0) printf("1 0 0");
	    else{
	        w = 1;
	        i = 0;
	    while (1>0){
	        a = i + 2;
	        b = i + 10;
	        c = i + 26;
	        if (n<=a){
	            printf("%ld 0 0\n",w);
	            break;
	        }
	        else if (n>a && n<=b){
	            printf("0 %ld 0\n",w);
	            break;
	        }
	        else if (n>b && n<=c){
	            printf("0 0 %ld\n",w);
	            break;
	        }
	        w = 2*w;
	        i += 26;
	    }
	        
	    }
	}
	return 0;
}

