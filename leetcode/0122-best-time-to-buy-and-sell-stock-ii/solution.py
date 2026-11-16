# Runtime: 1 ms
# Memory: 20.4 MB

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxi = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxi += prices[i] - prices[i-1]
        return maxi