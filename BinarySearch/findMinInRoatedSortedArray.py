class Solution:
    def findMin(self, nums: list[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[right]
    
ans = Solution()
nums = [1,2,3,5,7]
print(ans.findMin(nums=nums))