# Runtime: 3 ms
# Memory: 22.2 MB

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        if not nums:
            return []

        c1, c2 = None, None
        count1, count2 = 0, 0

        for num in nums:
            if num == c1:
                count1 += 1
            elif num == c2:
                count2 += 1
            elif count1 == 0:
                c1, count1 = num, 1
            elif count2 == 0:
                c2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        result = []
        t = len(nums) // 3
        for c in (c1, c2):
            if c is not None and nums.count(c) > t:
                result.append(c)

        return result