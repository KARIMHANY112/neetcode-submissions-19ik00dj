from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            # skip duplicates for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            L = i + 1
            R = len(nums) - 1

            while L < R:
                total = nums[i] + nums[L] + nums[R]

                if total > 0:
                    R -= 1
                elif total < 0:
                    L += 1
                else:  # total == 0
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1
                    # skip duplicates for L
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1

        return res