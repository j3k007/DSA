class Solution:

    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Sort the cars based on their position in descending order.
        right_to_Left = sorted(zip(position,speed), reverse=True)
        bottelneck = float("-inf")
        fleets = 0

        for d, s in right_to_Left:
            # Time each car take to reach to the target.
            timeToReachTarget = (target-d)/s
 
            if timeToReachTarget > bottelneck:
                bottelneck = timeToReachTarget
                fleets += 1 
       
        return fleets
    
ans = Solution()
target = 12
p = [10,8,0,5,3]
s = [2,4,1,1,3]
print(ans.carFleet(target=target, position=p, speed=s))