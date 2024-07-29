class Solutions:
    def sortColors(self, nums: list[int]) -> None:
        zeros = 0
        ones = 0
        n = len(nums)
        
        for num in range(n):
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
                
        for i in range(n):
            if i < zeros:
                nums[i] = 0
            elif zeros <= i < zeros + ones:
                nums[i] = 1
            else:
                nums[i] = 2