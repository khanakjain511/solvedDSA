# Runtime: 242 ms
# Memory: 21.6 MB

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