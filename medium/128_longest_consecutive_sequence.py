class Solution:
    
    # time complexity = O(2N) = O(N)
    # space complexity = O(2N) = Memory exceed
    # too much space + runtime
    def longest_consecutive(self, nums: list[int]) -> int:
        max_num = 1000000000
        sorted_array = [None] * max_num # 10^9
        minus_sorted_array = [None] * max_num
        
        for num in nums:
            if num >= 0:
                sorted_array[num] = 1
            else:
                minus_sorted_array[max_num - abs(num)] = 1
                
        arrays = minus_sorted_array + sorted_array
            
        ans = 0
        
        longest_consecutive = 0
        for i in arrays:
            if i is not None:
                longest_consecutive += 1
            else:
                ans = max(ans, longest_consecutive)
                longest_consecutive = 0
                
        return ans
    
    # time complexity = O(nlogn + n)
    # space complexity = O(1)
    def longest_consecutive_sorted(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums = sorted(nums, reverse=False)
        longest_consecutive = 1
        count = 1
        
        for i, num in enumerate(nums):
            if num - 1 == nums[i - 1]:
                count += 1
            elif num == nums[i - 1]:
                continue
            else:
                longest_consecutive = max(count, longest_consecutive)
                count = 1
        return max(count, longest_consecutive)
    
    # time complexity = 
    #   O(N) for building set
    #   O(N) for iterate through every element once
    #   O(N + N) = O(N)
    
    # space complextity = O(N)
    def longest_consecutive_neetcode_2nd(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        
        set_array = set(nums)
        
        visited = set()
        longest_consecutive = 1
        count = 1
        
        for num in set_array:
            if num in visited:
                continue
            
            visited.add(num)
            
            i = 1
            while num + i in set_array:
                count += 1
                visited.add(num + i)
                i += 1
                
            
            longest_consecutive = max(count, longest_consecutive)
            count = 1
            
        return longest_consecutive
                
    
solution = Solution()

print(solution.longest_consecutive_neetcode_2nd([1,2,0,1]))
print(solution.longest_consecutive_neetcode_2nd([0,3,7,2,5,8,4,6,0,1]))
print(solution.longest_consecutive_neetcode_2nd([100,4,200,1,3,2]))
print(solution.longest_consecutive_neetcode_2nd([0, -1]))