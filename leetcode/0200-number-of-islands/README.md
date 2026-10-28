# 200. Number of Islands

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Depth--First_Search-blue) ![Topic](https://img.shields.io/badge/Topic-Breadth--First_Search-blue) ![Topic](https://img.shields.io/badge/Topic-Union--Find-blue) ![Topic](https://img.shields.io/badge/Topic-Matrix-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 242 ms |
| Memory | 21.6 MB |
| Submission Date | 2026-10-28T04:32:27.308Z |
| Platform | leetcode |

## Problem Statement

<p>Given an <code>m x n</code> 2D binary grid <code>grid</code> which represents a map of <code>&#39;1&#39;</code>s (land) and <code>&#39;0&#39;</code>s (water), return <em>the number of islands</em>.</p>

<p>An <strong>island</strong> is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> grid = [
  [&quot;1&quot;,&quot;1&quot;,&quot;1&quot;,&quot;1&quot;,&quot;0&quot;],
  [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;1&quot;,&quot;0&quot;],
  [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;],
  [&quot;0&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;]
]
<strong>Output:</strong> 1
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> grid = [
  [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;],
  [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;],
  [&quot;0&quot;,&quot;0&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;],
  [&quot;0&quot;,&quot;0&quot;,&quot;0&quot;,&quot;1&quot;,&quot;1&quot;]
]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>m == grid.length</code>
- <code>n == grid[i].length</code>
- <code>1 &lt;= m, n &lt;= 300</code>
- <code>grid[i][j]</code> is <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.

## Solution

```py
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        columns = len(grid[0])
        count = 0

        def f(r, c):
            if r<0 or r>= rows or c<0 or c>= columns or grid[r][c]=='0':
                return
            
            grid[r][c] = '0'

            f(r+1, c)
            f(r-1, c)
            f(r, c+1)
            f(r, c-1)

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == '1':
                    f(r, c)
                    count+=1
        return count
```

[View on LeetCode](https://leetcode.com/problems/number-of-islands/)
