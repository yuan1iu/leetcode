# 218. The Skyline Problem
from heapq import heappop, heappush, heapify
def getSkyline(buildings): 
    entries = [(b[0], -b[2], b[1]) for b in buildings] # entry
    exits = set((b[1], 0, None) for b in buildings)
    events = sorted(entries + list(exits))
    heap, res = [(0, float('inf'))], [[0, 0]]
    for pos, height, end in events:
        while heap[0][1] <= pos: 
            h = heappop(heap)
        if height != 0: # entry
            heappush(heap, (height, end))
        if -heap[0][0] != res[-1][1]:
            res.append([pos, -heap[0][0]])
    return res[1:]
            

getSkyline([[1,3,3],[1,6,10]])

