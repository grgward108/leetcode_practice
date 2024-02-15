class Solution(object):
    def findMaxFish(self, grid):
        def dfs(r, c, visited):
            
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or (r, c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r, c))  
            value = grid[r][c]  

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                value += dfs(r + dr, c + dc, visited)

            return value

        maxFish = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:  
                    visited = set()  
                    maxFish = max(maxFish, dfs(i, j, visited))

        return maxFish