import math

class MySqrt:
    def __init__(self) -> None:
        pass

    def mySqrt(self, x: int) -> int:
        i = 1
        while x >= i * i:
            i += 1

        return int(i) - 1

    def mySqrt_binary_search(self, x: int) -> int:
        left = 0
        mid = 0
        right = x
        if x == 1:
            return 1

        while left < right:
            mid = math.floor((left + right) / 2)

            if mid * mid == x or left == mid:
                return mid
            elif mid * mid > x:
                right = mid
            else:
                left = mid
        return mid

    # python does not support tail resursive. That why it's much slower than while loop
    def mySqrt_binary_search_recursive(self, x: int) -> int:
        if x == 1:
            return 1

        def my_sqrt_binary_search(left, right) -> int:
            mid = math.floor((left + right) / 2)

            if mid * mid == x or left == mid:
                return mid
            elif mid * mid > x:
                return my_sqrt_binary_search(left, mid)
            else:
                return my_sqrt_binary_search(mid, right)
        return my_sqrt_binary_search(0, x)

def main():
    solution = MySqrt()
    print(solution.mySqrt_binary_search_recursive(4))
    print(solution.mySqrt_binary_search_recursive(27))

main()