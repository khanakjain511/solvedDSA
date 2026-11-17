# 1768. Merge Strings Alternately

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Two_Pointers-blue) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 41 ms |
| Memory | 19.1 MB |
| Submission Date | 2026-11-17T12:22:49.646Z |
| Platform | leetcode |

## Problem Statement

<p>You are given two strings <code>word1</code> and <code>word2</code>. Merge the strings by adding letters in alternating order, starting with <code>word1</code>. If a string is longer than the other, append the additional letters onto the end of the merged string.</p>

<p>Return <em>the merged string.</em></p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> word1 = &quot;abc&quot;, word2 = &quot;pqr&quot;
<strong>Output:</strong> &quot;apbqcr&quot;
<strong>Explanation:</strong>&nbsp;The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> word1 = &quot;ab&quot;, word2 = &quot;pqrs&quot;
<strong>Output:</strong> &quot;apbqrs&quot;
<strong>Explanation:</strong>&nbsp;Notice that as word2 is longer, &quot;rs&quot; is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
</pre>

<p>
```

**Example 3:**

```
</p>

<pre>
<strong>Input:</strong> word1 = &quot;abcd&quot;, word2 = &quot;pq&quot;
<strong>Output:</strong> &quot;apbqcd&quot;
<strong>Explanation:</strong>&nbsp;Notice that as word1 is longer, &quot;cd&quot; is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= word1.length, word2.length &lt;= 100</code>
- <code>word1</code> and <code>word2</code> consist of lowercase English letters.

## Solution

```py
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        i = 0
        n1, n2 = len(word1), len(word2)
        
        while i < n1 or i < n2:
            if i < n1:
                merged.append(word1[i])
            if i < n2:
                merged.append(word2[i])
            i += 1
            
        return "".join(merged)
```

[View on LeetCode](https://leetcode.com/problems/merge-strings-alternately/)
