class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid),len(grid[0])
        visit = set()

        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append([r,c])
                    visit.add((r,c))

        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        dist = 0
        while q:
            for _ in range(len(q)):
                i,j=q.popleft()
                grid[i][j]=dist
                for di,dj in directions:
                    newi,newj=i+di,j+dj
                    if newi<0 or newi>=rows or newj<0 or newj>=cols:
                        continue
                    if grid[newi][newj]!=2147483647 or (newi,newj) in visit:
                        continue

                    q.append([newi,newj])
                    visit.add((newi,newj))

            dist+=1
        