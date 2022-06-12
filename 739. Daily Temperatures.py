# 739. Daily Temperatures
def dailyTemperatures(temperatures):
    n = len(temperatures)
    hottest = 0
    answer = [0] * n
    
    for curr_day in range(n - 1, -1, -1):
        current_temp = temperatures[curr_day]
        if current_temp >= hottest:
            hottest = current_temp
            continue
        
        days = 1
        while temperatures[curr_day + days] <= current_temp:
            # Use information from answer to search for the next warmer day
            days += answer[curr_day + days]
        answer[curr_day] = days

    return answer

def dailyTemperatures_stack(temperatures):
    ans = [0] * len(temperatures)
    stack = []
    for idx, val in enumerate(temperatures):
        while stack and val > stack[-1][0]:
            temp, tempId = stack.pop()
            ans[tempId] = idx - tempId
        stack.append((val, idx))
    return ans
    
print(-1/2)