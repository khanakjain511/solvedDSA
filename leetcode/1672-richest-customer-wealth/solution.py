# Runtime: 1 ms
# Memory: 19.2 MB

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        m = len(accounts)
        n = len(accounts[0])
        maxi_arr = []
        for i in range(m):
            sums = 0
            for j in range(n):
                sums+= accounts[i][j]
            
            maxi_arr.append(sums)
        return max(maxi_arr)
        