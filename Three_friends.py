t=input()
for w in range(t):
        s=raw_input()
        l=s.split(" ")
        x=int(l[0])
        y=int(l[1])
        z=int(l[2])
        if x-y+z==0:
                print "yes"
        elif -x+y+z==0:
                print "yes"
        elif x+y-z==0:
                print "yes"
        elif x-y-z==0:
                print "yes"
        elif -x-y+z==0:
                print "yes"
        elif -x+y-z==0:
                print "yes"
        else:
                print "no"
        
