def letterCombinations(digits):
    d = {'2':'abc',
       '3':'def',
       '4':'ghi',
       '5':'jkl',
       '6':'mno',
       '7':'pqrs',
       '8':'tuv',
       '9':'wxyz'}
    result = []
    if digits == '':
        return result
    arr = [0]*len(digits)
    helper(digits,0,d,result,arr)
    return result

def helper(digits,index,d,result,arr):
    if index==len(digits):
        result.append(''.join(arr))
        return
    number = digits[index]
    candidates = list(d[number])
    for i in range(len(candidates)):
        arr[index] = candidates[i]
        helper(digits,index+1,d,result,arr)
        
ans = LetterCombinations('237')
print(len(ans))
print(ans)
