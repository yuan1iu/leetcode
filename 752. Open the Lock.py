# 752. Open the Lock
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
		# solve edge case '0000'
        if '0000' in deadends: return -1
        if target == '0000': return 0
        visit = set(deadends) # simply combine visit and deadends will make the code cleaner
        queue = collections.deque(['0000'])
        moves = 0
        while queue:
            moves += 1
            for n in range(len(queue)):
                num = queue.popleft()
                for i in range(4):
					# for each digit, we need to add 1 or minus 1
                    plus = num[:i]+str((int(num[i])+1)%10)+num[i+1:]
                    minus = num[:i]+str((int(num[i])-1)%10)+num[i+1:]
                    if plus == target or minus == target: return moves
					# then we push them into queue after checking not exisiting in deadends and visit
                    if plus not in visit:
                        queue.append(plus)
                        visit.add(plus)
                    if minus not in visit:
                        queue.append(minus)
                        visit.add(minus)    
        return -1