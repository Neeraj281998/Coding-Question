def string_compression(str):
  result=""
  count=0
  for i in range(len(str)):
    count+=1
    if i+1>=len(str) or str[i]!=str[i+1]:
      result+=str[i]+str(count)
      count=0
  if len(result)<len(str):
    return result
  else:
    return str
'''
INPUT :      a="aabcccccaaa"
OUTPUT  :  a2b1c5a3
'''
