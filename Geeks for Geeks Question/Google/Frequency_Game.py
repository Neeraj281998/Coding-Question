'''
Given an array A of size N. The elements of the array consists of positive integers. You have to find the largest element with minimum frequency.
'''

def LargButMinFreq(arr,n):
    memo={}
    for i in arr:
        if str(i) not in memo:
            memo[str(i)]=1
        else:
            memo[str(i)]+=1
    min=memo[list(memo)[0]]
    result=[]
    for key,value in memo.items():
        if value<min:
            result=result[int(key)]
            min=value
        elif value==min:
            result.append(int(key))
    return max(result)
