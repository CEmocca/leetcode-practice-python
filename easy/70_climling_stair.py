class ClimingStair:
    def __init__(self) -> None:
        pass

    # time complexity = 2^n because every fib() need to call another 2 fib()
    def climbStairs_brute_force(self, n: int) -> int:
        def fib(num: int) -> int:
            if num <= 1:
                return num
            return fib(num - 1) + fib(num - 2)
        return fib(n + 1)

    # time complexity = O(n)
    # space complexity = O(n)
    def climbStairs_memorization(self, n: int) -> int:
        mem = dict()
        def fib(num: int) -> int:
            if(num in mem):
                return mem[num]

            if num <= 1:
                mem[num] = num
                return mem[num]
            mem[num] = fib(num - 1) + fib(num - 2)
            return mem[num]
        return fib(n + 1)
        


def main():
    solution = ClimingStair()

    print(solution.climbStairs_brute_force(2))
    print(solution.climbStairs_brute_force(3))
    print(solution.climbStairs_brute_force(6))

    print(solution.climbStairs_memorization(2))
    print(solution.climbStairs_memorization(3))
    print(solution.climbStairs_memorization(6))

main()