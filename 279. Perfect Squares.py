# 279. Perfect Squares
import math
from collections import deque
class Solution():
    def numSquares(self, n):
        square_nums = [i**2 for i in range(1, int(math.sqrt(n))+1)]

        def minNumSquares(k):
            """ recursive solution """
            # bottom cases: find a square number
            if k in square_nums:
                return 1
            min_num = float('inf')

            # Find the minimal value among all possible solutions
            for square in square_nums:
                if k < square:
                    break
                new_num = minNumSquares(k-square) + 1
                min_num = min(min_num, new_num)
            return min_num

        return minNumSquares(n)

    def numSquares_bfs(self, n):
        squares = [i**2 for i in range(1,int(math.sqrt(n))+1)]
        queue = deque([n])
        level = 0
        while queue:
            level += 1
            for i in range(len(queue)):
                q = queue.popleft()
                for square in squares:
                    if q == square:
                        return level
                    elif square > q:
                        break
                    else: #square < q
                        queue.append(q-square)
