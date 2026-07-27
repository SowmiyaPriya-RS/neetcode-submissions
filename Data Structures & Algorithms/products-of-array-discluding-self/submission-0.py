class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = []
        prod = 1
        for i in range(len(nums)-1, 0, -1):
            suffix.append(prod)
            prod *= nums[i]
        suffix.append(prod)
        suffix = suffix[::-1]

        prefix = []
        prod = 1
        for i in range(len(nums)):
            prefix.append(prod)
            prod *= nums[i]
        print(prefix)

        for i in range(len(nums)):
            nums[i] = suffix[i]*prefix[i]

        return nums
        