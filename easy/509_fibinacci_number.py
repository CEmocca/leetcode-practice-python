

class Solution:

    def __init__(self):
        pass

    # time complexity is O(2^N)
    # space complexity is O(n)
    def fib(self, n: int) -> int:
        computed = {}
        def fib_tail(number: int) -> int:
            if number in computed:
                return computed[number]
            
            # base case
            if number <= 1:
                return number
            else:
                computed[number - 1] = fib_tail(number - 1)
                computed[number - 2] = fib_tail(number - 2)
                return computed[number - 1] + computed[number - 2]
        return fib_tail(n)
    

solution = Solution()

print(solution.fib(2))
print(solution.fib(3))
print(solution.fib(4))
print(solution.fib(5))
print(solution.fib(6))