# 304. Range Sum Query 2D - Immutable

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Design-blue) ![Topic](https://img.shields.io/badge/Topic-Matrix-blue) ![Topic](https://img.shields.io/badge/Topic-Prefix_Sum-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 177 ms |
| Memory | 33.4 MB |
| Submission Date | 2026-11-13T11:33:23.944Z |
| Platform | leetcode |

## Problem Statement

<p>Given a 2D matrix <code>matrix</code>, handle multiple queries of the following type:</p>

<ul>
	<li>Calculate the <strong>sum</strong> of the elements of <code>matrix</code> inside the rectangle defined by its <strong>upper left corner</strong> <code>(row1, col1)</code> and <strong>lower right corner</strong> <code>(row2, col2)</code>.</li>
</ul>

<p>Implement the <code>NumMatrix</code> class:</p>

<ul>
	<li><code>NumMatrix(int[][] matrix)</code> Initializes the object with the integer matrix <code>matrix</code>.</li>
	<li><code>int sumRegion(int row1, int col1, int row2, int col2)</code> Returns the <strong>sum</strong> of the elements of <code>matrix</code> inside the rectangle defined by its <strong>upper left corner</strong> <code>(row1, col1)</code> and <strong>lower right corner</strong> <code>(row2, col2)</code>.</li>
</ul>

<p>You must design an algorithm where <code>sumRegion</code> works on <code>O(1)</code> time complexity.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/sum-grid.jpg" style="width: 415px; height: 415px;" />
<pre>
<strong>Input</strong>
[&quot;NumMatrix&quot;, &quot;sumRegion&quot;, &quot;sumRegion&quot;, &quot;sumRegion&quot;]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
<strong>Output</strong>
[null, 8, 11, 12]

<strong>Explanation</strong>
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>m == matrix.length</code>
- <code>n == matrix[i].length</code>
- <code>1 &lt;= m, n &lt;= 200</code>
- <code>-10<sup>4</sup> &lt;= matrix[i][j] &lt;= 10<sup>4</sup></code>
- <code>0 &lt;= row1 &lt;= row2 &lt; m</code>
- <code>0 &lt;= col1 &lt;= col2 &lt; n</code>
- At most <code>10<sup>4</sup></code> calls will be made to <code>sumRegion</code>.

## Solution

```py
class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        rows, cols = len(matrix), len(matrix[0])
        # Extra row and column of 0s to handle boundary conditions cleanly
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for r in range(rows):
            for c in range(cols):
                self.prefix[r + 1][c + 1] = (
                    matrix[r][c]
                    + self.prefix[r][c + 1]
                    + self.prefix[r + 1][c]
                    - self.prefix[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefix[row2 + 1][col2 + 1]
            - self.prefix[row1][col2 + 1]
            - self.prefix[row2 + 1][col1]
            + self.prefix[row1][col1]
        )



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
```

[View on LeetCode](https://leetcode.com/problems/range-sum-query-2d-immutable/)
