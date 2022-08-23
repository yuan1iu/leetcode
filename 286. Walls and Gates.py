# 286. Walls and Gates
import collections


def wallsAndGates(rooms) -> None:
    visited = set()
    q = collections.deque()
    m, n = len(rooms), len(rooms[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in range(m):
        for j in range(n):
            if rooms[i][j] == 0:
                q.append((i, j))
                visited.add((i, j))
    while q:
        for i in range(len(q)):
            r, c = q.popleft()
            for x, y in dirs:
                next_r = r+x
                next_c = c+y
                if next_r == -1 or next_r == m or next_c == -1 or next_c == n or rooms[next_r][next_c] == -1 or (next_r, next_c) in visited:
                    continue
                q.append((next_r, next_c))
                visited.add(((next_r, next_c)))
                rooms[next_r][next_c] = rooms[r][c]+1
