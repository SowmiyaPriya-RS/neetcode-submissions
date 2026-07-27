class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        max_amount = 0
        left_max = height[l]
        right_max = height[r]

        while(l < r):
            if(left_max < right_max):
                l += 1
                left_max = max(height[l], left_max)
                max_amount += left_max - height[l]
            else:
                r -= 1
                right_max = max(height[r], right_max)
                max_amount += right_max - height[r]
        return max_amount
