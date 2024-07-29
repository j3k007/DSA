class Solution:
    def nextPermutation(self, nums: list[int])-> None:
        n = len(nums)
        brk = -1
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i + 1]:
                brk = i
                break
        
        if brk == -1:
            nums.sort()
            
        for i in range(n - 1, -1, -1):
            if nums[i] > nums[brk]:
                nums[i], nums[brk] = nums[brk], nums[i]
                break
        
        if brk + 1 != n - 1:
            l = nums[brk+1:]
            l.sort()
            nums[brk+1:]=l[:]
        