# cook your dish here
t=int(input())
while t:
	t=t-1
	n,a,b=input().split()
	n=int(n)
	a=int(a)
	b=int(b)
	l=list(map(int,input().split()))
	bob=alice=0
	for w in l:
		if w%a==0:
			bob+=1
		elif w%b==0:
			alice+=1
	if bob>alice:
		print("BOB")
	elif alice>bob:
		print("ALICE")
	else:
		print("ALICE")
