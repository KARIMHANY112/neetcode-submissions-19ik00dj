from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []

        for r in range(len(nums)):
            
            # 1. remove smaller elements
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()

            # 2. add current index
            dq.append(r)

            # 3. remove out-of-window
            l = r - k + 1
            if dq[0] < l:
                dq.popleft()

            # 4. add result
            if r >= k - 1:
                result.append(nums[dq[0]])

        return result