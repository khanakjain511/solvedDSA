# Runtime: 0 ms
# Memory: 19.1 MB

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k] = nums[i]
                k+=1
            
        return k