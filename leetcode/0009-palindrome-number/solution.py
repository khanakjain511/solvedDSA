# Runtime: 11 ms
# Memory: 19 MB

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
