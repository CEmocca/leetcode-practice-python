class MissingNumber:
    def __init__(self) -> None:
        pass


    def missingNumber(self, nums: list[int]) -> int:
        
        i = 1
        xor1 = 0

        while i <= len(nums):
            xor1 = xor1 ^ i
            i += 1

        j = 1
        xor2 = nums[0]

        while j < len(nums):
            xor2 = xor2 ^ nums[j]

            j += 1

        return xor1 ^ xor2

def main():
    solution = MissingNumber()
    print(solution.missingNumber([3,0,1]))
        
main()