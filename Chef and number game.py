t=int(input())
while t:
	t=t-1
	k=int(input())
	l=list(map(int,input().split()))
	m=n=0
	for w in l:
		if w<0:
			m+=1
		else:
			n+=1
	if m==0:
		print(n,n)
	elif n==0:
		print(m,m)
	else:
		if m<n:
			print(n,m)
		else:
			print(m,n)
	
