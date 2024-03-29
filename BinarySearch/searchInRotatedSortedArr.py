class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            
            # Check if first half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Check if second half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1          
        return -1
    
ans = Solution()
target = 2
nums = [4,5,6,7,0,1,2]
print(ans.search(nums, target))