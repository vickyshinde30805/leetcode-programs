
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        # Build original tree
        adj = [[] for _ in range(n)]

        for i in range(1, n):
            adj[parent[i]].append(i)

        # Store new parent relationships
        new_parent = parent[:]

        # Stack for each character
        stacks = [[] for _ in range(26)]

        # First DFS: Find closest matching ancestor
        def dfs1(u):
            c = ord(s[u]) - ord('a')

            if stacks[c]:
                new_parent[u] = stacks[c][-1]

            stacks[c].append(u)

            for v in adj[u]:
                dfs1(v)

            stacks[c].pop()

        dfs1(0)

        # Build modified tree
        tree = [[] for _ in range(n)]

        for i in range(1, n):
            tree[new_parent[i]].append(i)

        # Second DFS: Calculate subtree sizes
        ans = [1] * n

        def dfs2(u):
            for v in tree[u]:
                dfs2(v)
                ans[u] += ans[v]

        dfs2(0)

        return ans