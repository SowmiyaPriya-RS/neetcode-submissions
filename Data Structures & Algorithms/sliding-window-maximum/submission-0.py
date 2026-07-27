class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        l = 0
        while(l < len(nums)-k+1):
            temp = nums[l:l+k]
            largest = max(temp)
            result.append(largest)
            l += 1
        return result

        