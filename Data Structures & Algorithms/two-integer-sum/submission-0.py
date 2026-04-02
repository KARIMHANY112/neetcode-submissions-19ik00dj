class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in temp:
                return [temp[complement], i]
            temp[num] = i