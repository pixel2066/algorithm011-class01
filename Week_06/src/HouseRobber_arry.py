class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [ [None]*2 for i in range(n)]#创建二维矩阵，先2列，在n行

        if nums == None or n == 0 or n > 100:
            return 0

        #0：i房子不偷，1：i房子偷，dp[i][0]表示从0到第i个房子能偷到的最大值，同时第i个房子不偷
        dp[0][0] = 0         #初始化不偷状态
        dp[0][1] = nums[0]   #初始化偷状态

        
        for i in range(1,len(nums)):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1])#i-1个房子不偷，或偷的最大值
            dp[i][1] = dp[i-1][0] + nums[i]      

        return max(dp[n-1][0],dp[n-1][1])