class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        grid_copy = deepcopy(grid)

        fresh_c = 0
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid_copy[r][c]==2:
                    q.append((r,c))
                elif grid_copy[r][c]==1:
                    fresh_c+=1

        minutes=0
        while len(q) and fresh_c>0:
            minutes +=1

            total_rotten = len(q)

            for _ in range(total_rotten):
                i,j = q.popleft()
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    new_i,new_j= i+dx,j+dy
                    if new_i<0 or new_i==rows or new_j<0 or new_j==cols:
                        continue

                    if grid_copy[new_i][new_j]==0 or grid_copy[new_i][new_j]==2:
                        continue

                    fresh_c -=1
                    grid_copy[new_i][new_j]=2
                    q.append((new_i,new_j))

        if fresh_c>0:
            return -1
        return minutes















