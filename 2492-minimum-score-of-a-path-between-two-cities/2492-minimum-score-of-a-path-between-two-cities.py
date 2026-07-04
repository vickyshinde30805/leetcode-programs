class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        from collections import defaultdict
        
        graph = defaultdict(list)
        
        # Build graph
        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))
        
        visited = set()
        self.ans = float('inf')
        
        def dfs(node):
            visited.add(node)
            
            for nei, dist in graph[node]:
                # update minimum edge
                self.ans = min(self.ans, dist)
                
                if nei not in visited:
                    dfs(nei)
        
        dfs(1)
        return self.ans