class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid) 
        COLS = len(grid[0])

        def dfs(r, c): 
            # Stop if out of bounds or water/already visited. 
            if ( r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != "1" ): return 
        
            # Mark current land as visited. 
            grid[r][c] = "#" 

            # Explore all 4 directions. 
        
            dfs(r + 1, c) 
            dfs(r - 1, c) 
            dfs(r, c + 1) 
            dfs(r, c - 1)

        islands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1": islands += 1 
                # Mark the whole island visited. 
                dfs(r, c) 
        return islands






#                (row-1,col)
#                      ^
#                      |
# (row,col-1)   <-- (row,col) -->   (row,col+1)
#                       |

#                 (row+1,col)