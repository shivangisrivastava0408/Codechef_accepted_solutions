from fractions import Fraction
s=raw_input()
l=s.split(" ")
t=int(l[0])
for i in range(t):
	p=int(l[i+1])
	if p%2==0:
		s1=str(Fraction((2**p)-1,3*(2**p)))
		h=s1.index('/')
		print s1[0:h],s1[h+1:],
	else:
		s2=str(Fraction((2**p)+1,3*(2**p)))
		f=s2.index('/')
		print s2[0:f],s2[f+1:],
