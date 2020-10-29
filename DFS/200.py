def isOk(x, y, m, n):
    return x >= 0 and y >= 0 and x < m and y < n 

class Solution:
    def numIslands((self, grid: List[List[str]]) -> int:)
        if len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        def dfs(x, y):
            visited[x][y] = True
            xRows = [-1, 1, 0, 0]
            yCols = [0, 0, -1, 1]
            for i in range(4):
                new_x = x + xRows[i]
                new_y = y + yCols[i]
                if isOk(new_x, new_y, m, n) and not visited[new_x][new_y] and grid[new_x][new_y] == '1':
                    dfs(new_x, new_y)
        cnt = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == '1':
                    dfs(i, j)
                    cnt += 1
        
        return cnt