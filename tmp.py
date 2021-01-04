import collections
class Solution:
    def transpose(self, matrix):
        return [[x[i] for x in matrix] for i in range(len(matrix[0]))]

    def maxSlidingWindow(self, nums, k: int):
        window = collections.deque()
        res = []
        for i in range(len(nums)):
            if window and window[0] <= i - k:
                window.popleft()
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res



sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))
