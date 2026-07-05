class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)

        score = [[-1] * n for _ in range(n)]
        ways = [[0] * n for _ in range(n)]

        score[n - 1][n - 1] = 0
        ways[n - 1][n - 1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if board[i][j] == "X" or board[i][j] == "S":
                    continue

                for x, y in ((i + 1, j), (i, j + 1), (i + 1, j + 1)):
                    if x >= n or y >= n or score[x][y] == -1:
                        continue

                    if score[x][y] > score[i][j]:
                        score[i][j] = score[x][y]
                        ways[i][j] = ways[x][y]

                    elif score[x][y] == score[i][j]:
                        ways[i][j] = (ways[i][j] + ways[x][y]) % MOD

                if score[i][j] != -1 and board[i][j].isdigit():
                    score[i][j] += int(board[i][j])

        if score[0][0] == -1:
            return [0, 0]

        return [score[0][0], ways[0][0] % MOD]
        