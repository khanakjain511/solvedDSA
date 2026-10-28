# Runtime: 308 ms
# Memory: 96.7 MB

class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        stack = [source]
        visited = {source}

        while stack:
            curr = stack.pop()
            if curr == destination:
                return True
            
            for neighbour in graph[curr]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)
        return False