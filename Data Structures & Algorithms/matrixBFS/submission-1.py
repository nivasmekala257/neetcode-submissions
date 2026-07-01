class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        visit=set()
        queue=deque()
        queue.append((0,0))
        visit.add((0,0))
        length=0

        while queue:
            for i in range(len(queue)):
                r,c=queue.popleft()
                if r == ROWS-1 and c == COLS-1:
                    return length
                
                neighbors=[[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in neighbors:
                    r = r+dr
                    c = c+dc
                    if (min(r,c)<0 or 
                        r == ROWS or c == COLS or
                        (r,c)in visit or 
                        grid[r][c] ==1):
                        continue
                    queue.append((r,c))
                    visit.add((r,c))
            length +=1
        return -1