# Runtime: 3 ms
# Memory: 21.2 MB

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