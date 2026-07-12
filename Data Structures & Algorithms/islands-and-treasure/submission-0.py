class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid),len(grid[0])
        visit = set()
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))

        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        dist = 0
        while q:
            for _ in range(len(q)):

                i,j = q.popleft()
                grid[i][j]=dist
                for dx,dj in directions:
                    x,y = i+dx , j +dj

                    if x<0 or x>= rows or y<0 or y>=cols or (x,y) in visit:
                        continue
                    if grid[x][y] !=  2147483647:
                        continue
                    visit.add((x,y))
                    q.append([x,y])
            dist+=1
                
