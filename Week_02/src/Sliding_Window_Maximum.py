class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_q = []
        visited = set()
        res = []
        for i in range(k):
            heapq.heappush(max_q,(-nums[i], i))
        visited.add(0)
        res = [-max_q[0][0]]
        for i in range(k, len(nums)):
            heapq.heappush(max_q, (-nums[i], i))
            while max_q and max_q[0][1] in visited:
                heapq.heappop(max_q)
            res.append(-max_q[0][0])
            visited.add(i-k+1)
        return res