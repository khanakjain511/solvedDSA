# 14. Longest Common Prefix

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Topic](https://img.shields.io/badge/Topic-Trie-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 19.2 MB |
| Submission Date | 2026-11-10T11:30:49.327Z |
| Platform | leetcode |

## Problem Statement

<p>Write a function to find the longest common prefix string amongst an array of strings.</p>

<p>If there is no common prefix, return an empty string <code>&quot;&quot;</code>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> strs = [&quot;flower&quot;,&quot;flow&quot;,&quot;flight&quot;]
<strong>Output:</strong> &quot;fl&quot;
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> strs = [&quot;dog&quot;,&quot;racecar&quot;,&quot;car&quot;]
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> There is no common prefix among the input strings.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= strs.length &lt;= 200</code>
- <code>0 &lt;= strs[i].length &lt;= 200</code>
- <code>strs[i]</code> consists of only lowercase English letters if it is non-empty.

## Solution

```py
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        for i in range(len(strs[0])):
            char = strs[0][i]

            for s in strs[1:]:
                if i == len(s) or s[i] != char:
                    return strs[0][:i]
        
        return strs[0]
```

[View on LeetCode](https://leetcode.com/problems/longest-common-prefix/)
