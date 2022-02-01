#Given Two String ,Write a method if str2 is a permutation of the str1

def arePermutation(str1, str2):
    if len(str1)>len(str2):
        return False
    count=[0]*256
    i=0
    for i in range(len(str1)-1):
        count[ord(str1[i])]+=1
        count[ord(str2[i])]-=1
    if count!=([0]*256):
        return False
    return True

print(arePermutation('abca','bzaa')) 
