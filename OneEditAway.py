def oneEditAway(str1,str2):
    len1=len(str1)
    len2=len(str2)
    if abs(len1-len2)>1:
        return False
    count=0
    i,j=0,0
    while i<len1 and j<len2:
        if str1[i]!=str2[j]:
            if count ==1:
                return False
            if len1>len2:
                i+=1
            elif len1<len2:
                j+=1
            else:
                i+=1
                j+=1
            count+=1
        else:
            i+=1
            j+=1
    if i<len1 or j<len2:
        count+=1
    return count==1

print(oneEditAway("pale","ple"))
