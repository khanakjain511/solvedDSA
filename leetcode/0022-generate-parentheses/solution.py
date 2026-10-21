# Runtime: 0 ms
# Memory: 19.5 MB

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        curr = []
        ans = []

        def f(i, opn, close):
            if len(curr)==2*n:
                ans.append(''.join(curr))
                return
            
            if opn<n:
                curr.append('(')
                f(i+1, opn+1, close)
                curr.pop()

            if close<opn:
                curr.append(')')
                f(i+1, opn, close+1)
                curr.pop()
        f(0, 0, 0)
        return ans