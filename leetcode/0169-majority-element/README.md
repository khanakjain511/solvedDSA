# 169. Majority Element

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Hash_Table-blue) ![Topic](https://img.shields.io/badge/Topic-Divide_and_Conquer-blue) ![Topic](https://img.shields.io/badge/Topic-Sorting-blue) ![Topic](https://img.shields.io/badge/Topic-Counting-blue) ![Topic](https://img.shields.io/badge/Topic-Boyer–Moore_Majority_Vote_Algorithm-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 23 ms |
| Memory | 21.4 MB |
| Submission Date | 2026-10-20T19:01:25.181Z |
| Platform | leetcode |

## Problem Statement

<p>Given an array <code>nums</code> of size <code>n</code>, return <em>the majority element</em>.</p>

<p>The majority element is the element that appears more than <code>&lfloor;n / 2&rfloor;</code> times. You may assume that the majority element always exists in the array.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>
<pre><strong>Input:</strong> nums = [3,2,3]
<strong>Output:</strong> 3
</pre><p>
```

**Example 2:**

```
</p>
<pre><strong>Input:</strong> nums = [2,2,1,1,1,2,2]
<strong>Output:</strong> 2
</pre>
<p>&nbsp;</p>
```

## Constraints

- <code>n == nums.length</code>
- <code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code>
- <code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code>
- The input is generated such that a majority element will exist in the array.

## Solution

```py
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dict = {}
        leng = len(nums)//2
        for i in nums:
            dict[i] = dict.get(i, 0) + 1

            if dict[i] > leng:
                return i
```

[View on LeetCode](https://leetcode.com/problems/majority-element/)
