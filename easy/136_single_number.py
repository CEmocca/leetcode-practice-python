class SingleNumber:
    
    def __init__(self) -> None:
        pass

    def singleNumber(self, nums: list[int]) -> int:
        count_dict = dict()

        i = 0
        while i < len(nums):
            if nums[i] not in count_dict:
                count_dict[nums[i]] = 1
            else:
                count_dict[nums[i]] = count_dict[nums[i]] + 1

            i += 1 
        
        for key, value in count_dict.items():
            if value == 1:
                return key


def main():
    solution = SingleNumber()
    print(solution.singleNumber([2,2,1]))
    print(solution.singleNumber([4,1,2,1,2]))
    print(solution.singleNumber([1]))

main()