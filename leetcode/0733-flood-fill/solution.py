# Runtime: 4 ms
# Memory: 20.2 MB

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        s_color = image[sr][sc]

        if s_color == color:
            return image
        
        rows = len(image)
        colums = len(image[0])

        def f(r, c):
            if r<0 or r>= rows or c<0 or c>= colums:
                return
            
            if image[r][c] != s_color:
                return
            
            image[r][c] = color

            f(r+1, c)
            f(r-1, c)
            f(r, c+1)
            f(r, c-1)
        
        f(sr, sc)
        return image