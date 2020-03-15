# cook your dish here
l1=[[1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25],
    [26,27,28,29,30]]
    
l,r,u,d=0,4,0,5
while(l<r and u<d):
    for w in range(l,r+1):
        print(l1[u][w]," ",)
    u+=1
    for w in range(u,d+1):
        print(l1[w][r]," ",)
    r-=1
    for w in range(r,l-1,-1):
        print(l1[d][w]," ",)
    d-=1
    for w in range(d,u-1,-1):
        print(l1[w][l]," ",)
    l+=1
 
if(l<r):
    for w in range(l,r+1):
        print(l1[u][w]," ",)
if(u<d):
    for w in range(u,d+1):
        print(l1[w][l]," ",)
        
