Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



#### SOLUTION

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        n = len(strs)
        i = 0 
        min_lenght = float('inf')
        for s in strs:
            if len(s) < min_length:
                min_length = len(s)
                
        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    returns s[:i]
            i +=1
        return strs[0][:i]
