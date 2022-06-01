# 118. Pascal's Triangle
def generate(numRows: int):
    res = [[1]]
    for n in range(1,numRows):
        row = [1]*(n+1)
        for i in range(1,len(row)-1):
            row[i] = res[n-1][i-1] + res[n-1][i]
        res.append(row)
    return res