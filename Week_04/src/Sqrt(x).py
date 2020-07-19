class Solution:
    def mySqrt(self, x: int) -> int:
        #考虑0的情况
        if not x:
            return 0
        #从1起始
        left, right = 1, x // 2
        while left < right:
            # 注意：这里一定取右中位数，如果取左中位数，代码可能会进入死循环
            # mid = left + (right - left + 1) // 2
            mid = (left + right + 1) // 2
            if mid * mid > x:
                right = mid -1
            else:
                left = mid
        return left