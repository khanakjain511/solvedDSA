# Runtime: 14 ms
# Memory: 19.2 MB

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
