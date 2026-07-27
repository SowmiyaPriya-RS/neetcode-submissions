class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        hashmap = {}
        for i in range(n):
            if nums[i] in hashmap:
                return True
            else:
                hashmap[nums[i]] = 1
        return False

        