class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid),len(grid[0])

        def dfs(r,c):
            if not (0<=r<rows and 0<=c < cols):
                return
            if grid[r][c]!="1":
                return

            grid[r][c]="#"

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        island = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    island+=1

                dfs(r,c)

        return island