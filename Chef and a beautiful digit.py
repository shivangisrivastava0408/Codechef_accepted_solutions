# cook your dish here
t=int(input())
while t:
	t=t-1
	l=input().split()
	n,d=l[0],l[1]
	s=[]
	k=len(n)
	for w in range(k-1,-1,-1):
		if s==[] and n[w]<d:
			s.append(n[w])
		elif len(s)>0 and n[w]<=s[-1]:
			s.append(n[w])
	p=''
	m=len(s)
	for w in range(m-1,-1,-1):
		p+=s[w]
	for w in range(k-m):
		p+=d
	print(p)


