

class Solution:

    def __init__(self):
        pass
    
    # time complexity is O(N ^ 2)
    # space complexity is O(1)
    def brute_force_num_identical_pairs(self, nums: list[int]) -> int:
        ans = 0
        num_len = len(nums)
        i = 0
        while i < num_len:
            j = i + 1
            while j < num_len:
                if nums[i] == nums[j]:
                    ans += 1
                    
                j += 1
            i += 1

        return ans

    # time complexity is O(N)
    # space complexity is O(N)
    def num_identical_pairs(self, nums: list[int]) -> int:
        ans = 0
        visited = dict()
        
        for num in nums:
            if num in visited:
                ans += visited[num]
                visited[num] = visited[num] + 1
            else:
                visited[num] = 1

        return ans
    

solution = Solution()

print(solution.num_identical_pairs([1,2,3,1,1,3]))
print(solution.num_identical_pairs([1,1,1,1]))
print(solution.num_identical_pairs([1,2,3]))