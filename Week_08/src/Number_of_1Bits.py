class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            res = n % 2
            if res == 1:
                count += 1
            n //= 2 #取整除结果在引用给n，直到n整除为0
        return count