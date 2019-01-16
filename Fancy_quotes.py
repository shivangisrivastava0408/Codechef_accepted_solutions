t=int(input())
while t:
	t=t-1
	s=input().split(" ")
	if "not" in s:
		print('Real Fancy')
	else:
		print('regularly fancy')
