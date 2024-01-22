

class Solution:

    def __init__(self):
        pass

    # time complexity is O(N)
    # space complexity is O(1)
    def number_of_employees_who_met_target(self, hours: list[int], target: int) -> int:
        ans = 0
        
        for hour in hours:
            if hour >= target:
                ans += 1
                
        return ans
    

solution = Solution()

print(solution.number_of_employees_who_met_target([0,1,2,3,4], 2))
print(solution.number_of_employees_who_met_target([5,1,4,2,2], 6))