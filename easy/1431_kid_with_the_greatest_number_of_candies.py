

class Solution:

    def __init__(self):
        pass

    # time complexity is O(N^2)
    # space complexity is O(1)
    def kids_with_candies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candy = max(candies)
        
        ans = []
        for candy in candies:
            if candy + extraCandies >= max_candy:
                ans.append(True)
            else:
                ans.append(False)
                
        return ans
    

solution = Solution()

print(solution.kids_with_candies([2,3,5,1,3], 3))
print(solution.kids_with_candies([4,2,1,1,2], 1))
print(solution.kids_with_candies([12,1,12], 10))