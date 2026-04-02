class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        left_max = height[l]
        right_max = height[r]
        water = 0

        while l < r:
            if left_max < right_max:
                l += 1
                if height[l] < left_max:
                    water += left_max - height[l]
                else:
                    left_max = height[l]
            else:
                r -= 1
                if height[r] < right_max:
                    water += right_max - height[r]
                else:
                    right_max = height[r]

        return water