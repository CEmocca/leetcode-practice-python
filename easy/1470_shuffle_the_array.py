

class Solution:

    def __init__(self):
        pass

    # time complexity is O(N)
    # space complexity is O(N)
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        ans = []
        
        i = 0
        while (i < n):
            ans.append(nums[i])
            ans.append(nums[i + n])
            i += 1

        return ans
    

solution = Solution()

print(solution.shuffle([2,5,1,3,4,7], 3))
# [2, 4, 1, 3, 5, 7]
# [2, 4, 3, 1, 5, 7]
print(solution.shuffle([1,2,3,4,4,3,2,1], 4))
print(solution.shuffle([1,1,2,2], 2))