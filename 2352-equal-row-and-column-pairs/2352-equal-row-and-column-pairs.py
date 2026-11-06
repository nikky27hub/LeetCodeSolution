class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        row_count = {}

        # Store frequency of each row
        for row in grid:
            key = tuple(row)
            row_count[key] = row_count.get(key, 0) + 1

        count = 0

        # Check each column
        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))
            count += row_count.get(col, 0)

        return count
        