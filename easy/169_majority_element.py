class MajorityElement:
    def __init__(self) -> None:
        pass

    def majorityElement(self, nums: list[int]) -> int:
        count_dict = dict()

        i = 0
        while i < len(nums):
            if nums[i] not in count_dict:
                count_dict[nums[i]] = 1
            else:
                count_dict[nums[i]] = count_dict[nums[i]] + 1

            i += 1

        max = 0
        max_val = 0
        for key, value in count_dict.items():
            if value > max:
                max_val = key
                max = value

        return max_val

def main():
    solution = MajorityElement()
    print(solution.majorityElement([3,2,3]))
    print(solution.majorityElement([2,2,1,1,1,2,2]))

main()