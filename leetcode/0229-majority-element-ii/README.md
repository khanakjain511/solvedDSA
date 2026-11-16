# 229. Majority Element II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Hash_Table-blue) ![Topic](https://img.shields.io/badge/Topic-Sorting-blue) ![Topic](https://img.shields.io/badge/Topic-Counting-blue) ![Topic](https://img.shields.io/badge/Topic-Boyer–Moore_Majority_Vote_Algorithm-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 3 ms |
| Memory | 22.2 MB |
| Submission Date | 2026-11-16T03:56:21.700Z |
| Platform | leetcode |

## Problem Statement

<p>Given an integer array of size <code>n</code>, find all elements that appear more than <code>&lfloor;n / 3&rfloor;</code> times.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> nums = [3,2,3]
<strong>Output:</strong> [3]
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> nums = [1]
<strong>Output:</strong> [1]
</pre>

<p>
```

**Example 3:**

```
</p>

<pre>
<strong>Input:</strong> nums = [1,2]
<strong>Output:</strong> [1,2]
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></code>
- <code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code>

## Solution

```py
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
```

[View on LeetCode](https://leetcode.com/problems/majority-element-ii/)
