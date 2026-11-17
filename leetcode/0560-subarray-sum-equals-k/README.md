# 560. Subarray Sum Equals K

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Hash_Table-blue) ![Topic](https://img.shields.io/badge/Topic-Prefix_Sum-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 30 ms |
| Memory | 21.7 MB |
| Submission Date | 2026-11-17T05:42:05.065Z |
| Platform | leetcode |

## Problem Statement

<p>Given an array of integers <code>nums</code> and an integer <code>k</code>, return <em>the total number of subarrays whose sum equals to</em> <code>k</code>.</p>

<p>A subarray is a contiguous <strong>non-empty</strong> sequence of elements within an array.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>
<pre><strong>Input:</strong> nums = [1,1,1], k = 2
<strong>Output:</strong> 2
</pre><p>
```

**Example 2:**

```
</p>
<pre><strong>Input:</strong> nums = [1,2,3], k = 3
<strong>Output:</strong> 2
</pre>
<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code>
- <code>-1000 &lt;= nums[i] &lt;= 1000</code>
- <code>-10<sup>7</sup> &lt;= k &lt;= 10<sup>7</sup></code>

## Solution

```py
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

```

[View on LeetCode](https://leetcode.com/problems/subarray-sum-equals-k/)
