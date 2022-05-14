class Solution:
    def subsets(self, nums):
        def backtrack(first=0, curr=[]):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
                return
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output

    def subsets2(self, nums):
        res = []
        subset = []

        def dfs(index):
            if index >= len(nums):
                res.append(subset[:])
                return
            subset.append(nums[index])
            dfs(index + 1)

            subset.pop()
            dfs(index + 1)

        dfs(0)
        return res

    def subsets3(self, nums):
        ret = []
        self.dfs3(nums, [], ret)
        return ret

    def dfs3(self, nums, path, res):
        res.append(path)
        for i in range(len(nums)):
            self.dfs3(nums[i+1:], path+[nums[i]], res)

    def subsets4(self, nums):
        res = []

        def dfs(sub, i):
            print(sub)
            res.append(sub[:])
            for j in range(i, len(nums)):
                sub.append(nums[j])
                dfs(sub, j+1)
                sub.pop()
        dfs([], 0)
        return res


s = Solution()
print(s.subsets3([1, 2, 3]))
