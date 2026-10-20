# Runtime: 23 ms
# Memory: 21.4 MB

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dict = {}
        leng = len(nums)//2
        for i in nums:
            dict[i] = dict.get(i, 0) + 1

            if dict[i] > leng:
                return i