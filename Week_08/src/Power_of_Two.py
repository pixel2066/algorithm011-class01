class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # n二进制最高位为1,其余所有位为0
        # n−1二进制最高位为0,其余所有位为1
        return n > 0 and n & (n-1) == 0