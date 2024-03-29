class Solution:
    def search(self, nums: list[int], target:int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r)//2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1
    
ans = Solution()
target = 2
nums = [4,5,6,7,0,1,2]
print(ans.search(nums=nums, target=target))