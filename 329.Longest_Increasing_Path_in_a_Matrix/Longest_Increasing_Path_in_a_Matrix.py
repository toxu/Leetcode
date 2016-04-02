class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        h = len(matrix)
        if h == 0: return 0
        w = len(matrix[0])
        dp = [[0] * w for x in range(h)]
        for x in range(h):
            for y in range(w):
                dp[x][y] = self.dfs(x, y, matrix, dp)
        return max(max(x) for x in dp)

    def dfs(self, x, y, matrix, dp):
        for dx, dy in zip([1,0,-1,0], [0,1,0,-1]):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] > matrix[x][y]:
                if not dp[nx][ny]:
                    dp[nx][ny] = self.dfs(nx, ny, matrix, dp)
                dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)
        dp[x][y] = max(dp[x][y], 1)
        return dp[x][y]


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        h = len(matrix)
        if h == 0: return 0
        w = len(matrix[0])
        dp = [[0] * w for i in range(h)]
        pre = -1
        for x in range(h):
            for y in range(w):
                dp[x][y] = self.dfs(x, y, matrix, dp, pre)
        return max(max(x) for x in dp)

    def dfs(self, x, y, matrix, dp, pre):
        def isValid(x, y, matrix):
            return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])
        if matrix[x][y] <= pre:
            return 0
        if dp[x][y] != 0:
            return dp[x][y]
        if isValid(x+1, y, matrix):
            dp[x][y] = max(dp[x][y], self.dfs(x+1, y, matrix, dp, matrix[x][y])+1)
        if isValid(x-1, y, matrix):
            dp[x][y] = max(dp[x][y], self.dfs(x-1, y, matrix, dp, matrix[x][y])+1)
        if isValid(x, y+1, matrix):
            dp[x][y] = max(dp[x][y], self.dfs(x, y+1, matrix, dp, matrix[x][y])+1)
        if isValid(x, y-1, matrix):
            dp[x][y] = max(dp[x][y], self.dfs(x, y-1, matrix, dp, matrix[x][y])+1)
        dp[x][y] = max(dp[x][y], 1)
        return dp[x][y]
