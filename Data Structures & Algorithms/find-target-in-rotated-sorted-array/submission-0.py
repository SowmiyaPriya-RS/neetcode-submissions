class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while(l < r):
            mid = (l+r)//2
            if(nums[r] < nums[mid]):
                l = mid+1
            elif(nums[r] > nums[mid]):
                r = mid

        split = l
        l = 0
        r = len(nums)-1

        if(target >= nums[split] and target <= nums[r]):
            l = split
        else:
            r = split-1

        while(l <= r):
            mid = (l+r)//2
            if(nums[mid] < target):
                l = mid+1
            elif(nums[mid] > target):
                r = mid-1
            else:
                return mid

        return -1