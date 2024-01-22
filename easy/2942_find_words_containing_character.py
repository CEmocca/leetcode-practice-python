

class Solution:

    def __init__(self):
        pass

    # time complexity is O(N^2)
    # space complexity is O(1)
    def maximum_wealth(self, accounts: list[list[int]]) -> int:
        richest = 0
        
        for account in accounts:
            sum_account = 0
            for bank in account:
                sum_account += bank
                
            richest = max(richest, sum_account)

        return richest
    

solution = Solution()

print(solution.maximum_wealth([[1,2,3],[3,2,1]]))
print(solution.maximum_wealth([[1,5],[7,3],[3,5]]))