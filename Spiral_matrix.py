def spiralOrder(arr):
    top = 0
    bottom = len(arr)-1
    left = 0
    right = len(arr[0])-1
    dir = 0
    res = []
    while (top <= bottom and left <=right):    
        if dir ==0:
            for i in range(left,right+1): 
                res.append(arr[top][i])
            top +=1
            dir = 1

        elif dir ==1:
            for i in range(top,bottom+1): 
                res.append(arr[i][right])
            right -=1 
            dir = 2
            
        elif dir ==2:
            for i in range(right,left-1,-1): 
                res.append(arr[bottom][i])
            bottom -=1
            dir = 3
            
        elif dir ==3:
            for i in range(bottom,top-1,-1): 
                res.append(arr[i][left])
            left +=1
            dir = 0
    return res

if __name__ == '__main__':
    row = input().split()
    n = int(row[0])
    m = int(row[1])
    grid = []
    for i in range(n):
        nums = input().split()
        nums = [int(i) for i in nums]
        grid.append(nums)
    result = spiralOrder(grid)
    print(result)
    
