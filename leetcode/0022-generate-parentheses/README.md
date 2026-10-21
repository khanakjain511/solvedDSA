# 22. Generate Parentheses

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Topic](https://img.shields.io/badge/Topic-Backtracking-blue) ![Topic](https://img.shields.io/badge/Topic-Bracket_Sequences-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 19.5 MB |
| Submission Date | 2026-10-21T14:22:23.566Z |
| Platform | leetcode |

## Problem Statement

<p>Given <code>n</code> pairs of parentheses, write a function to <em>generate all combinations of well-formed parentheses</em>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>
<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> ["((()))","(()())","(())()","()(())","()()()"]
</pre><p>
```

**Example 2:**

```
</p>
<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> ["()"]
</pre>
<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= n &lt;= 8</code>

## Solution

```py
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        curr = []
        ans = []

        def f(i, opn, close):
            if len(curr)==2*n:
                ans.append(''.join(curr))
                return
            
            if opn<n:
                curr.append('(')
                f(i+1, opn+1, close)
                curr.pop()

            if close<opn:
                curr.append(')')
                f(i+1, opn, close+1)
                curr.pop()
        f(0, 0, 0)
        return ans
```

[View on LeetCode](https://leetcode.com/problems/generate-parentheses/)
