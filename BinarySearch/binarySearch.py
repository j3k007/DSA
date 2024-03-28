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
lst = [-1, -2, -3, -4, 0, 1, 2, 3, 4]
t = 3
print(ans.search(lst, t))