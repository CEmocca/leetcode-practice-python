

class Solution:

    def __init__(self):
        pass

    # time complexity is O(n)
    # space complexity is O(n)
    def get_concatenation(self, nums: list[int]) -> list[int]:
        num_len = len(nums)
        ans = [None] * (num_len * 2)

        for index, num in enumerate(nums):
            ans[index] = num
            ans[index + num_len] = num

        return ans
    

solution = Solution()

print(solution.get_concatenation([1, 2, 1]))