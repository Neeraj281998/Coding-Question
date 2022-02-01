#URLify a given string (Replace spaces is %20)

def URLify(string):
    string=string.strip()
    org_length=len(string)
    no_of_space=string.count(' ')
    new_length=org_length+no_of_space*2
    index=new_length-1
    
    string=list(string)
    for i in range(org_length-1,new_length-1):
        string.append('0')
    for i in range(org_length-1,-1,-1):
        if string[i]==" ":
            string[index]="0"
            string[index-1]="2"
            string[index-2]="%"
            index-=3
        else:
            string[index]=string[i]
            index-=1
    return ''.join(string)

print(URLify("Mr John Smith "))
