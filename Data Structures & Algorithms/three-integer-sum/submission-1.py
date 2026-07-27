class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []
        i = 0

        while(i < n-2):
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            j = i+1
            k = n-1
            while(j < k):
                if(nums[j]+nums[k] > -nums[i]):
                    k -= 1
                elif(nums[j]+nums[k] < -nums[i]):
                    j += 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
            i += 1 
        return result

        