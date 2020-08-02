class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if nums == None or n == 0 or n > 100:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        res = max(dp[0],dp[1])
        
        for i in range(2,n):
            dp[i] = max(dp[i-1],dp[i-2] + nums[i])
            res = max(res,dp[i])
        return res