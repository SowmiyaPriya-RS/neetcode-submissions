class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        seq = set(nums)

        for i in nums:
            if i-1 not in seq:
                length = 1
                while i+length in seq:
                    length += 1
                longest = max(longest, length)
        
        return longest
        