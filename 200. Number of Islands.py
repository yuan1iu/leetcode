# 200. Number of Islands
import collections
class solution:
    def numIslands_dfs(self, grid) -> int:
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c] != '1':
                return
            grid[r][c] = '#'
            print(r,c)
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
        ans = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    # start dfs  
                    dfs(i,j)
                    ans+=1
        return ans

    def numIslands_bfs(self, grid) -> int:
        ans = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    # start bfs
                    queue = collections.deque()
                    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
                    queue.append((i,j))
                    while queue:    
                        r,c = queue.popleft()
                        for dx, dy in dirs:
                            x = r + dx
                            y = c + dy
                            if x>=0 and x<rows and y>=0 and y<cols and grid[x][y] == '1':
                                grid[x][y] = '#'
                                queue.append((x,y))
                    ans += 1        
        return ans