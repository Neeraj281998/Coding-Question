class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    memo={}
    left=0
    right=0
    max_length=0
    while right<len(s):
        if s[right] in memo and memo[s[right]]>=left:
            left=memo[s[left]]+1
        max_length=max(max_length,right-left+1)
        memo[s[right]]=right
        right+=1
    return max_length
    
   
        
