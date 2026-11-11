# 912. Sort an Array

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Divide_and_Conquer-blue) ![Topic](https://img.shields.io/badge/Topic-Sorting-blue) ![Topic](https://img.shields.io/badge/Topic-Heap_(Priority_Queue)-blue) ![Topic](https://img.shields.io/badge/Topic-Merge_Sort-blue) ![Topic](https://img.shields.io/badge/Topic-Bucket_Sort-blue) ![Topic](https://img.shields.io/badge/Topic-Radix_Sort-blue) ![Topic](https://img.shields.io/badge/Topic-Counting_Sort-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 624 ms |
| Memory | 28.4 MB |
| Submission Date | 2026-11-11T18:13:15.352Z |
| Platform | leetcode |

## Problem Statement

<p>Given an array of integers <code>nums</code>, sort the array in ascending order and return it.</p>

<p>You must solve the problem <strong>without using any built-in</strong> functions in <code>O(nlog(n))</code> time complexity and with the smallest space complexity possible.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> nums = [5,2,3,1]
<strong>Output:</strong> [1,2,3,5]
<strong>Explanation:</strong> After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> nums = [5,1,1,2,0,0]
<strong>Output:</strong> [0,0,1,1,2,5]
<strong>Explanation:</strong> Note that the values of nums are not necessarily unique.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></code>
- <code>-5 * 10<sup>4</sup> &lt;= nums[i] &lt;= 5 * 10<sup>4</sup></code>

## Solution

```py
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)

    def merge(self, left: list[int], right: list[int]) -> list[int]:
        sorted_arr = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1

        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])
        return sorted_arr
```

[View on LeetCode](https://leetcode.com/problems/sort-an-array/)
