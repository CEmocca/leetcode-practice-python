class Solution:
    def two_sum_neetcode_150_problems(self, numbers: list[int], target: int) -> list[int]:
        
        i = 0
        j = len(numbers) - 1
        
        while i < j:
            sum = numbers[i] + numbers[j]
            if sum == target:
                break
            elif sum > target:
                j -= 1
            else:
                i += 1
        
        return [i + 1, j + 1]