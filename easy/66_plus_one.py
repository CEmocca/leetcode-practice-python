import math

class PlusOne:
    def __init__(self) -> None:
        pass

    def plusOne_brute_force(self, digits: list[int]) -> list[int]:
        carry = 0
        c_index = last_index = len(digits) - 1
        results = []

        while c_index >= 0:
            sum = 0
            if c_index == last_index:
                sum = digits[c_index] + 1
            else:
                sum = digits[c_index] + carry

            carry = math.floor(sum / 10)
            results.append(sum % 10)     

            c_index -= 1
        
        if(carry == 1):
            results.append(carry)
        results.reverse()
        return results

    def plusOne_recursive(self, digits: list[int]) -> list[int]:
        def plus_one(nums: list[int], carry: int, sums: list[int]) -> list[int]:
            if carry == 1 and not nums:
                return [1] + sums
            if not nums:
                return sums

            sum = nums[-1] + carry
            next_carry = math.floor(sum / 10)
            digit = sum % 10

            return plus_one(nums[:-1], next_carry, [digit] + sums)

        return plus_one(digits, 1, [])
            

def main():
    solution = PlusOne()
    print(solution.plusOne_brute_force([1,2,3]))
    print(solution.plusOne_brute_force([4,3,2,1]))
    print(solution.plusOne_brute_force([9]))

    print(solution.plusOne_recursive([1,2,3]))
    print(solution.plusOne_recursive([4,3,2,1]))
    print(solution.plusOne_recursive([9]))

main()