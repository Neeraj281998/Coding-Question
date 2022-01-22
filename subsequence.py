#Print subsequences
def subseq(s,main):
    if main=="":
        print(s)
        return
    ch=main[0]
    subseq(s+ch,main[1:])
    subseq(s,main[1:]) 

subseq("","abc")

#Print subsequences in Array 


def subseq(s,main):
    if main=="":
        list=[]
        list.append(s)
        return list
    ch=main[0]
    left=subseq(s+ch,main[1:])
    right=subseq(s,main[1:]) 

    left+=right
    return left

print(subseq("","abc"))
