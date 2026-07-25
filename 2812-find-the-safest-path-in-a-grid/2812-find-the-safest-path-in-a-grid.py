class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[-1] * n for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < n and 0 <= nc < n
                        and dist[nr][nc] == -1):
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        pq = [(-dist[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]

        while pq:
            safety, r, c = heapq.heappop(pq)
            safety = -safety

            if visited[r][c]:
                continue

            visited[r][c] = True

            if r == n - 1 and c == n - 1:
                return safety

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < n and 0 <= nc < n
                        and not visited[nr][nc]):

                        new_safety = min(safety, dist[nr][nc])
                        heapq.heappush(
                        pq,
                        (-new_safety, nr, nc)
                    )





        