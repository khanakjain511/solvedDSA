# Runtime: 0 ms
# Memory: 19.2 MB

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        for i in range(len(strs[0])):
            char = strs[0][i]

            for s in strs[1:]:
                if i == len(s) or s[i] != char:
                    return strs[0][:i]
        
        return strs[0]