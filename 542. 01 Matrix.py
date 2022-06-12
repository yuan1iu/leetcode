# 542. 01 Matrix
from collections import deque 
class Solution:

    def updateMatrix(self, mat):
        def bfs(r, c, dis):
            if r >= 0 and r < ROWS and c >= 0 and c < COLS \
                and (r, c) not in visited and mat[r][c] != 0:
                queue.append((r, c, dis))
                visited.add((r,c))
                mat[r][c] = dis

        ROWS = len(mat)
        COLS = len(mat[0])
        queue = deque()
        visited = set()
        for i in range(ROWS):
            for j in range(COLS):
                if mat[i][j] == 0: # start from 0s
                    queue.append((i, j, 0))
                    visited.add((i, j))
        while queue:           
            r, c, dis = queue.popleft()
            bfs(r + 1, c, dis + 1)
            bfs(r - 1, c, dis + 1)
            bfs(r, c + 1, dis + 1)
            bfs(r, c - 1, dis + 1)


        return