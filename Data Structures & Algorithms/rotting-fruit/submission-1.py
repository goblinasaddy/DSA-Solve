class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid),len(grid[0])

        q = deque()
        fresh_c = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh_c +=1

        minutes = 0
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        while q and fresh_c>0:
            
            minutes+=1
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    newr,newc = r+dr,c+dc
                    if newr<0 or newr>=rows or newc<0 or newc>=cols or grid[newr][newc]!=1:
                        continue
                    grid[newr][newc]=2
                    q.append((newr,newc))
                    fresh_c-=1

        if fresh_c>0:
            return -1
        return minutes
