t=int(input())
while t:
	t=t-1
	n=int(input())
	l={}
	k=0
	for w in range(n):
		s=input()
		p=''
		if 'a' in s:
			p+='1'
		else:
			p+='0'
		if 'e' in s:
			p+='1'
		else:
			p+='0'
		if 'i' in s:
			p+='1'
		else:
			p+='0'
		if 'o' in s:
			p+='1'
		else:
			p+='0'
		if 'u' in s:
			p+='1'
		else:
			p+='0'
		if p in l:
			l[p]+=1
		else:
			l[p]=1
	d=list(l.keys())
	for i in range(len(d)-1):
		for j in range(i+1,len(d),1):
			g=int(d[i],2) |int(d[j],2)
			if int(bin(g)[2:])==11111:
				k+=l[d[i]]*l[d[j]]
	a=l['11111']
	i=1
	for w in range(a):
		k+=a-i
		i+=1
	print(k)
