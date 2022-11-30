class RemoveDup:
    def __init__(self) -> None:
        pass

    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        # because if nums is not empty then we already have 1 distinct value
        distinct_element = 1

        for i in range(1, len(nums)):
            if(nums[i] != nums[i - 1]):
                nums[distinct_element] = nums[i]
                distinct_element += 1
        return distinct_element


def main():
    solution = RemoveDup()
    print(solution.removeDuplicates([1,1,2]))
    print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

    aa = [1,2,3]
    aa[0] = 4
    print(aa)

main()