class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total= m*n
        k %= total

        arr = []
        for row in grid:
            arr.extend(row)

        arr = arr[-k:] + arr[:-k]

        result = []
        id=0
        for i in range(m):
            result.append(arr[id:id+n])
            id += n

        return result
        