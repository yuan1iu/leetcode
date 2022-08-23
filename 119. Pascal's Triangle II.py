# 119. Pascal's Triangle II
class Solution:
    def getRow(self, rowIndex: int):
        def pascal(r, c):
            if c == 0 or c == r:
                return 1
            return pascal(r-1, c) + pascal(r-1, c-1)
        res = []
        for i in range(rowIndex+1):
            res.append(pascal(rowIndex,i))
        return res

    def getRow2(self, rowIndex: int):
        row = []
        for i in range(rowIndex+1):
            for j in range(i - 1, 0, -1):
                row[j]  = row[j] + row[j - 1]
            row.append(1)
        return row
s = Solution()
s.getRow2(4)