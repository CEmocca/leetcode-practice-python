

class Solution:

    def __init__(self):
        pass

    # time complexity is O(n)
    # space complexity is O(n)
    def build_array(self, nums: list[int]) -> list[int]:
        ans = [None] * len(nums)
        
        for i, _ in enumerate(nums):
            ans[i] = nums[nums[i]]
            
        return ans
    

solution = Solution()

print(solution.build_array([0,2,1,5,3,4]))