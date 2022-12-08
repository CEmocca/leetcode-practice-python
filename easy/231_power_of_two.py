class PowerOfTwo:
    def __init__(self) -> None:
        pass

    def isPowerOfTwo(self, n: int) -> bool:
        power_result = 1
        if n == 1:
            return True

        
        while power_result <= n:
            power_result *= 2
            if power_result == n:
                return True
            
        return False


def main():
    solution = PowerOfTwo()
    print(solution.isPowerOfTwo(1))

main()