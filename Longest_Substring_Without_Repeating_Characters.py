class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        last=0
        maxVal=0
        memo={}
        while last<len(s):
            if s[last] in memo and memo[s[last]]>=start:
                start=memo[s[last]]+1    
            maxVal=max(maxVal,last-start+1)
            memo[s[last]]=last
            last+=1
        return maxVal    
        