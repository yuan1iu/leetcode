# 84. Largest Rectangle in Histogram
def largestRectangleArea(heights) -> int:
    def helper(start, end):
        if start > end: return 0
        if start == end: return heights[start]
        minId = start
        for i in range(start, end+1):
            if heights[i] < heights[minId]:
                minId = i
        cur = heights[minId] * (end-start+1)
        left = helper(start, minId-1)
        right = helper(minId+1, end)
        return max(cur,left, right)
    return helper(0,len(heights)-1)



print(largestRectangleArea([4,2]))
