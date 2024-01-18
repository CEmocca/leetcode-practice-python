

class Solution:

    def __init__(self):
        pass

    # time complexity is O(N)
    # space complexity is O(1)
    def final_value_after_perations(self, operations: list[str]) -> int:
        ans = 0
        
        for op in operations:
            match op:
                case '++X':
                    ans += 1
                case 'X++':
                    ans += 1
                case '--X':
                    ans -= 1
                case 'X--':
                    ans -= 1

        return ans
    

solution = Solution()

print(solution.num_identical_pairs([1,2,3,1,1,3]))
print(solution.num_identical_pairs([1,1,1,1]))
print(solution.num_identical_pairs([1,2,3]))