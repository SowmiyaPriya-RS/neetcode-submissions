class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        n = len(nums)
        result = []

        for i in range(n):
            val = target - nums[i]
            if nums[i] in hashmap:
                result.append(hashmap[nums[i]])
                result.append(i)
                return result
            else:
                hashmap[val] = i
        
        