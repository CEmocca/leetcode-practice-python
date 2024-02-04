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
    
    def longest_consecutive_sorted(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        
        sorted_array = sorted(nums, reverse=False)
        print(sorted_array)
        longest_consecutive = 1
        count = 1
        
        for i, num in enumerate(sorted_array):
            print(f'num - 1 = {num - 1} == {sorted_array[i - 1]}, count = {count}')
            if num - 1 == sorted_array[i - 1]:
                count += 1
            elif num == sorted_array[i - 1]:
                continue
            else:
                longest_consecutive = max(count, longest_consecutive)
                count = 1
        return max(count, longest_consecutive)

                
    
solution = Solution()

print(solution.longest_consecutive_sorted([1,2,0,1]))
print(solution.longest_consecutive_sorted([0,3,7,2,5,8,4,6,0,1]))