    # from collections import defaultdict

class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:

        graph = defaultdict(list)

        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))

        visited = set()
        ans = float("inf")

        def dfs(city):
            nonlocal ans

            visited.add(city)

            for nxt, dist in graph[city]:
                ans = min(ans, dist)

                if nxt not in visited:
                    dfs(nxt)

        dfs(1)

        return ans