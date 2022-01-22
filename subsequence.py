def subseq(s,main):
    if main=="":
        print(s)
        return
    ch=main[0]
    subseq(s+ch,main[1:])
    subseq(s,main[1:]) 

subseq("","abc")
