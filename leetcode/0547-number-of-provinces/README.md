# 547. Number of Provinces

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Depth--First_Search-blue) ![Topic](https://img.shields.io/badge/Topic-Breadth--First_Search-blue) ![Topic](https://img.shields.io/badge/Topic-Union--Find-blue) ![Topic](https://img.shields.io/badge/Topic-Graph_Theory-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 3 ms |
| Memory | 21.2 MB |
| Submission Date | 2026-10-28T04:19:06.425Z |
| Platform | leetcode |

## Problem Statement

<p>There are <code>n</code> cities. Some of them are connected, while some are not. If city <code>a</code> is connected directly with city <code>b</code>, and city <code>b</code> is connected directly with city <code>c</code>, then city <code>a</code> is connected indirectly with city <code>c</code>.</p>

<p>A <strong>province</strong> is a group of directly or indirectly connected cities and no other cities outside of the group.</p>

<p>You are given an <code>n x n</code> matrix <code>isConnected</code> where <code>isConnected[i][j] = 1</code> if the <code>i<sup>th</sup></code> city and the <code>j<sup>th</sup></code> city are directly connected, and <code>isConnected[i][j] = 0</code> otherwise.</p>

<p>Return <em>the total number of <strong>provinces</strong></em>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/24/graph1.jpg" style="width: 222px; height: 142px;" />
<pre>
<strong>Input:</strong> isConnected = [[1,1,0],[1,1,0],[0,0,1]]
<strong>Output:</strong> 2
</pre>

<p>
```

**Example 2:**

```
</p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/24/graph2.jpg" style="width: 222px; height: 142px;" />
<pre>
<strong>Input:</strong> isConnected = [[1,0,0],[0,1,0],[0,0,1]]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= n &lt;= 200</code>
- <code>n == isConnected.length</code>
- <code>n == isConnected[i].length</code>
- <code>isConnected[i][j]</code> is <code>1</code> or <code>0</code>.
- <code>isConnected[i][i] == 1</code>
- <code>isConnected[i][j] == isConnected[j][i]</code>

## Solution

```py
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        province = 0

        def f(city: int):
            for neighbour in range(n):
                if isConnected[city][neighbour] == 1 and not visited[neighbour]:
                    visited[neighbour] = True
                    f(neighbour)
            
        for i in range(n):
            if not visited[i]:
                province +=1
                visited[i] = True
                f(i)
        
        return province
```

[View on LeetCode](https://leetcode.com/problems/number-of-provinces/)
