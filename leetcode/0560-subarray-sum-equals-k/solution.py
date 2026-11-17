# Runtime: 30 ms
# Memory: 21.7 MB

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        prefix_counts = {0: 1}
        
        for num in nums:
            curr_sum += num
            
            diff = curr_sum - k
            if diff in prefix_counts:
                count += prefix_counts[diff]
                
            prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1
            
        return count
